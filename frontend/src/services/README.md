# src/services/

App-wide technical services (not feature logic):

- `api-client.ts` → the ONE axios instance. Features define their endpoints in
  `features/<x>/api/` but always use this client — never `fetch`/`axios` directly.
- Future: `auth.ts` (token storage/refresh), `analytics.ts`, etc.

Why: auth headers, error mapping, timeouts and retries are handled once,
consistently, instead of copy-pasted across features.
