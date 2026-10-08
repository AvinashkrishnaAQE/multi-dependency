# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: pricing.spec.ts >> applies 10% discount
- Location: tests/pricing.spec.ts:4:5

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: 170
Received: 180
```

# Test source

```ts
  1 | import { test, expect } from '@playwright/test';
  2 | import { applyDiscount } from '../src/pricing';
  3 | 
  4 | test('applies 10% discount', () => {
  5 |   // 10% off 200 is 180
> 6 |   expect(applyDiscount(200, 10)).toBe(170);
    |                                  ^ Error: expect(received).toBe(expected) // Object.is equality
  7 | });
  8 | 
```