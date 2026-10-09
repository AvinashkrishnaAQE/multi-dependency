import { test, expect } from '@playwright/test';
import { applyDiscount } from '../src/pricing';

test('applies 10% discount', () => {
  // 10% off 200 is 180
  expect(applyDiscount(200, 10)).toBe(180);
});
