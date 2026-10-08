import fs from 'fs';
import path from 'path';

const STATE_DIR = path.join(__dirname, '..', 'data', 'state');

export function readState<T>(name: string, fallback: T): T {
  const file = path.join(STATE_DIR, `${name}.json`);
  if (!fs.existsSync(file)) return fallback;
  return JSON.parse(fs.readFileSync(file, 'utf-8')) as T;
}

export function writeState(name: string, value: unknown): void {
  fs.mkdirSync(STATE_DIR, { recursive: true });
  fs.writeFileSync(path.join(STATE_DIR, `${name}.json`), JSON.stringify(value, null, 2));
}
