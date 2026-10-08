import { test, expect } from '@playwright/test';
import { formatPrice } from '../lib/money';

test('formats price with two decimals', () => {
  expect(formatPrice(5)).toBe('$5.00');
});
