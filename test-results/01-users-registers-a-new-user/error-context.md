# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: 01-users.spec.ts >> registers a new user
- Location: tests/01-users.spec.ts:4:5

# Error details

```
Error: expect(received).toContain(expected) // indexOf

Expected substring: "@shop.com"
Received string:    "qa_bob@shop.test"
```

# Test source

```ts
  1  | import { test, expect } from '@playwright/test';
  2  | import { writeState } from '../src/store';
  3  | 
  4  | test('registers a new user', () => {
  5  |   const newUser = { username: 'qa_bob', email: 'qa_bob@shop.test' };
  6  |   // Registration only accepts addresses on the shop's test domain.
> 7  |   expect(newUser.email).toContain('@shop.com');
     |                         ^ Error: expect(received).toContain(expected) // indexOf
  8  |   writeState('users', { [newUser.username]: newUser });
  9  | });
  10 | 
```