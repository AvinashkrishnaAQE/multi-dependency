# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: format.spec.ts >> formats price with two decimals
- Location: tests/format.spec.ts:4:5

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: "$5.00"
Received: "$5"
```

# Test source

```ts
  1 | import { test, expect } from '@playwright/test';
  2 | import { formatPrice } from '../lib/money';
  3 | 
  4 | test('formats price with two decimals', () => {
> 5 |   expect(formatPrice(5)).toBe('$5.00');
    |                          ^ Error: expect(received).toBe(expected) // Object.is equality
  6 | });
  7 | 
```