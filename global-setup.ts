import fs from 'fs';
import path from 'path';

// Every run starts from a clean shared state folder.
export default async function globalSetup() {
  const dir = path.join(__dirname, 'data', 'state');
  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir, { recursive: true });
}
