import { test, expect } from '@playwright/test';

test('adds 18% tax', () => {
  const net = 100;
  // 18% tax on 100 is 118
  expect(Math.round(net * 1.18)).toBe(119);
});
