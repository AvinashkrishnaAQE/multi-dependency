# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: 02-profile.spec.ts >> edits the profile
- Location: tests/02-profile.spec.ts:4:5

# Error details

```
Error: User 'qa_bob' not found

expect(received).toBeDefined()

Received: undefined
```

# Test source

```ts
  1  | import { test, expect } from '@playwright/test';
  2  | import { readState, writeState } from '../src/store';
  3  | 
  4  | test('edits the profile', () => {
  5  |   const users = readState<Record<string, { username: string; email: string }>>('users', {});
  6  |   const bob = users['qa_bob'];
> 7  |   expect(bob, "User 'qa_bob' not found").toBeDefined();
     |                                          ^ Error: User 'qa_bob' not found
  8  |   writeState('users', { ...users, qa_bob: { ...bob, email: 'bob@shop.test' } });
  9  | });
  10 | 
```