# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: stock.spec.ts >> counts items in stock
- Location: tests/stock.spec.ts:3:5

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: 4
Received: 3
```

# Test source

```ts
  1 | import { test, expect } from '@playwright/test';
  2 | 
  3 | test('counts items in stock', () => {
  4 |   const stock = ['pen', 'book', 'lamp'];
> 5 |   expect(stock.length).toBe(4);
    |                        ^ Error: expect(received).toBe(expected) // Object.is equality
  6 | });
  7 | 
```