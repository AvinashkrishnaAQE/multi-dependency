# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: 04-totals.spec.ts >> shows totals in USD
- Location: tests/04-totals.spec.ts:4:5

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: "USD"
Received: "EUR"
```

# Test source

```ts
  1 | import { test, expect } from '@playwright/test';
  2 | import { readState } from '../src/store';
  3 | 
  4 | test('shows totals in USD', () => {
  5 |   const settings = readState('settings', { currency: 'USD' });
> 6 |   expect(settings.currency).toBe('USD');
    |                             ^ Error: expect(received).toBe(expected) // Object.is equality
  7 | });
  8 | 
```