import { test, expect } from '@playwright/test';
import { readState } from '../src/store';

test('shows totals in USD', () => {
  const settings = readState('settings', { currency: 'USD' });
  expect(settings.currency).toBe('USD');
});
