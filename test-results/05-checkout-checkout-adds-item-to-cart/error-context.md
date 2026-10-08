# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: 05-checkout.spec.ts >> checkout >> adds item to cart
- Location: tests/05-checkout.spec.ts:7:7

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: 2
Received: 1
```

# Test source

```ts
  1  | import { test, expect } from '@playwright/test';
  2  | import { Cart } from '../src/cart';
  3  | 
  4  | test.describe.serial('checkout', () => {
  5  |   const cart = new Cart();
  6  | 
  7  |   test('adds item to cart', () => {
  8  |     cart.add('book');
> 9  |     expect(cart.count).toBe(2);
     |                        ^ Error: expect(received).toBe(expected) // Object.is equality
  10 |   });
  11 | 
  12 |   test('pays for the order', () => {
  13 |     expect(cart.count).toBeGreaterThan(0);
  14 |   });
  15 | });
  16 | 
```