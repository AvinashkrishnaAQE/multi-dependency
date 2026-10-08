import { test, expect } from '@playwright/test';

test('counts items in stock', () => {
  const stock = ['pen', 'book', 'lamp'];
  expect(stock.length).toBe(4);
});
