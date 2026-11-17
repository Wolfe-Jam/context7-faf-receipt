import { test } from 'node:test';
import assert from 'node:assert/strict';
import { app } from '../src/app.js';

test('GET /health', async () => {
  const server = app.listen(0);
  const { port } = server.address();
  const r = await fetch(`http://127.0.0.1:${port}/health`);
  assert.equal(r.status, 200);
  server.close();
});
