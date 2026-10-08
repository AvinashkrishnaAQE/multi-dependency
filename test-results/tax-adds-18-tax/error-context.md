# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: tax.spec.ts >> adds 18% tax
- Location: tests/tax.spec.ts:3:5

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: 119
Received: 118
```

# Test source

```ts
  1 | import { test, expect } from '@playwright/test';
  2 | 
  3 | test('adds 18% tax', () => {
  4 |   const net = 100;
  5 |   // 18% tax on 100 is 118
> 6 |   expect(Math.round(net * 1.18)).toBe(119);
    |                                  ^ Error: expect(received).toBe(expected) // Object.is equality
  7 | });
  8 | 
```