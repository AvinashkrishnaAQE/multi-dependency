"""Live myAstra run on the fixture project, as mySDET would delegate one repair cycle.

Usage: python live_myastra.py <cycle> <all_at_once|one_by_one> [reject_tests_csv]
Runs from mydiya-agents/. Real LLM, real isolation reruns, real code fixer.
Cards are answered by script; everything shown/answered is logged.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
import time
import uuid

sys.path.insert(0, "agents")
from dotenv import load_dotenv  # noqa: E402

load_dotenv(".env")

import logging  # noqa: E402

logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(name)s %(message)s")
for name in ("myAstraOrchestrator", "myAstra"):
    logging.getLogger(name).setLevel(logging.INFO)
logging.getLogger("langsmith").setLevel(logging.CRITICAL)

from langchain_core.messages import HumanMessage  # noqa: E402
from langgraph.checkpoint.memory import InMemorySaver  # noqa: E402
from langgraph.types import Command  # noqa: E402

from shared import loop_contracts as lc  # noqa: E402
from shared.llm.factory import LLMFactory  # noqa: E402
from myAstraOrchestrator.src.orchestration.graph import create_orchestrator  # noqa: E402
from myAstraOrchestrator.src.orchestration.lifecycle import run_segment  # noqa: E402

PROJECT = os.path.abspath("agents/scm_workspace/worktrees/myastra-live-test")
OUT = os.path.dirname(os.path.abspath(__file__))

cycle = int(sys.argv[1])
mode = sys.argv[2]
reject = set(filter(None, (sys.argv[3] if len(sys.argv) > 3 else "").split(",")))
excluded = json.loads(os.environ.get("EXCLUDED_SIGS", "[]"))
previous = json.loads(os.environ.get("PREVIOUS_ATTEMPTS", "[]"))

wid = "live1"
vid = f"{wid}:v{cycle}"
log: list[dict] = []


def note(kind: str, **data):
    entry = {"t": round(time.time() - START, 1), "kind": kind, **data}
    log.append(entry)
    print(json.dumps(entry, default=str)[:3000], flush=True)


def answer(payload: dict) -> dict:
    gate = payload.get("gate")
    chips = [c.get("id") for c in payload.get("chips") or []]
    detail = payload.get("detail") or {}
    note("card", gate=gate, title=payload.get("title"), chips=chips, summary=payload.get("summary"),
         files=detail.get("files"), rca=str(detail.get("rca") or "")[:2500], diff=str(detail.get("diff") or "")[:2500])
    if gate in ("decision_branch", "doubt"):
        chip = mode if mode in chips else chips[0]
    elif gate == "patch_approval":
        files = set(detail.get("files") or [])
        chip = "reject" if files and files <= reject else "approve"
    else:
        chip = "approve" if "approve" in chips else chips[0]
    out = {"chip": chip, "gate_id": payload.get("gate_id")}
    if chip == "reject":
        out["text"] = "Not this one, live-test rejection."
    note("answer", gate=gate, chip=chip)
    return out


async def main():
    llm = LLMFactory.from_env()
    checkpointer = InMemorySaver()
    state = {
        "playwright_project_path": PROJECT,
        "publish_mode": lc.PUBLISH_DEFERRED,
        "repair_context": {
            "workflow_id": wid, "validation_id": vid, "cycle": cycle, "max_cycles": 3,
            "excluded_patch_signatures": excluded, "force_repo_wide": False, "previous_attempts": previous,
        },
        "validation_result": {
            "validation_id": vid, "workflow_id": wid,
            "report_path": os.path.join(PROJECT, ".myvega-runs", f"run-{cycle}", "report.normalized.json"),
            "artifacts_dir": os.path.join(PROJECT, ".myvega-runs", f"run-{cycle}"), "failures": [],
        },
        "interaction_mode": "ask_each",
        "gate_scope": f"wf:{wid}:c{cycle}",
        "resolved_gates": {},
        "messages": [HumanMessage(content=(
            f"Repair cycle {cycle} of 3: diagnose validation {vid}. Its report is at report_path in your "
            "state; read only that. Diagnose EVERY failing test that read_failure_report records, "
            "delegating to ONE specialist at a time. Then call apply_approved_patch ONCE: it asks the "
            "user whether to fix them all at once or one by one, applies the small fixes, and hands the "
            "bigger ones to myGenie as one proposal -- the tests are re-run once, after all of them. "
            "Do not open a pull request."))],
    }
    config = {"configurable": {"thread_id": f"live-{cycle}-{uuid.uuid4().hex[:6]}"},
              "metadata": {"live_test": f"cycle{cycle}-{mode}"}}
    graph = create_orchestrator(llm, checkpointer=checkpointer, store=None, state=state)
    result = await run_segment(lambda: graph, state, config)
    while result.get("__interrupt__"):
        payload = result["__interrupt__"][0].value
        result = await run_segment(lambda: graph, Command(resume=answer(payload)), config)

    calls = []
    for m in result.get("messages") or []:
        for tc in getattr(m, "tool_calls", None) or []:
            args = tc.get("args") or {}
            calls.append(f"{tc.get('name')}" + (f"[{args.get('subagent_type')}]" if args.get("subagent_type") else "")
                         + (f"({args.get('test_name')})" if args.get("test_name") else ""))
    note("tool_calls", sequence=calls)
    note("final", status=result.get("status"), step=result.get("current_step"),
         errors=result.get("errors"), tokens=result.get("token_usage_totals"))
    note("rca", findings=[{k: r.get(k) for k in ("test_name", "issue_type", "confidence", "root_cause",
                                                  "dependency_status", "depends_on", "patches")}
                          for r in result.get("rca_results") or []])
    note("isolation", runs=result.get("isolation_rerun_results"))
    note("skipped", tests=result.get("skipped_tests"))
    note("astra_result", value=result.get("astra_result"))
    note("fix_proposal", value=result.get("fix_proposal"))
    note("fix_log", value=result.get("fix_log"), fixed_files=result.get("fixed_files"))
    with open(os.path.join(OUT, f"live_cycle{cycle}_{mode}.json"), "w") as f:
        json.dump(log, f, indent=2, default=str)


START = time.time()
asyncio.run(main())
