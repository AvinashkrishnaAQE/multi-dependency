import { test, expect } from '@playwright/test';
import { readState, writeState } from '../src/store';

test('edits the profile', () => {
  const users = readState<Record<string, { username: string; email: string }>>('users', {});
  const bob = users['qa_bob'];
  expect(bob, "User 'qa_bob' not found").toBeDefined();
  writeState('users', { ...users, qa_bob: { ...bob, email: 'bob@shop.test' } });
});
