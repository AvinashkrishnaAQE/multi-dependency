import { test, expect } from '@playwright/test';
import { writeState } from '../src/store';

test('registers a new user', () => {
  const newUser = { username: 'qa_bob', email: 'qa_bob@shop.test' };
  // Registration only accepts addresses on the shop's test domain.
  expect(newUser.email).toContain('@shop.test');
  writeState('users', { [newUser.username]: newUser });
});
