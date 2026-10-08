import { test, expect } from '@playwright/test';
import { readState, writeState } from '../src/store';

test('switches currency to EUR', () => {
  writeState('settings', { currency: 'EUR' });
  expect(readState('settings', { currency: 'USD' }).currency).toBe('EUR');
});
