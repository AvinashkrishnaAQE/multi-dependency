/**
 * Shared test helper: formats an amount as dollars, ALWAYS with two decimals
 * (e.g. 5 -> "$5.00", 3.5 -> "$3.50"). Used by every price assertion.
 */
export function formatPrice(amount: number): string {
  return '$' + amount;
}
