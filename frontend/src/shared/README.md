# src/shared/

Reusable building blocks used by **two or more features**.

- `components/` → design-system/UI-kit components (Button, Modal, Table…)
- `hooks/`      → generic hooks (useDebounce, useLocalStorage…)
- `utils/`      → pure helper functions (date/number formatting…)
- `constants/`  → app-wide constants (routes, config keys…)

Rules:
- Nothing here may import from `features/` — dependency flows one way:
  `features → shared`, never the reverse.
- Don't move something here "just in case" — promote it only when a second
  feature actually needs it.
