import { test, expect } from '@playwright/test';
import { Cart } from '../src/cart';

test.describe.serial('checkout', () => {
  const cart = new Cart();

  test('adds item to cart', () => {
    cart.add('book');
    expect(cart.count).toBe(1);
  });

  test('pays for the order', () => {
    expect(cart.count).toBeGreaterThan(0);
  });
});
