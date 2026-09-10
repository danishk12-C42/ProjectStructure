# src/features/

**One folder per feature — this is the heart of our conflict-free structure.**

Each feature is self-contained:

```
features/
  orders/
    components/   → UI components used ONLY by this feature
    hooks/        → React hooks used ONLY by this feature
    api/          → API calls for this feature (uses shared api-client)
    types/        → TypeScript types for this feature
    index.ts      → the feature's public exports (its "API" to the rest of the app)
```

Rules:
- A feature may import from `shared/` and `services/`, and from another
  feature's `index.ts` only — never from another feature's internals.
- If a component/hook is needed by 2+ features, move it to `shared/`.
- `features/example/` shows the expected layout — copy it for new features,
  delete it once real features exist.

Why: two developers on different features touch different folders → minimal
merge conflicts; a broken feature doesn't ripple through the app.
