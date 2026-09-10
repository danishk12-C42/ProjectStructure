# src/store/

Global client state (if/when needed — start without it!).

Guidance:
- Server data (lists, entities from the API) → use TanStack Query in the
  feature's `api/` folder, NOT a global store.
- True global UI state (current user, theme) → add Zustand or Redux Toolkit
  here, one slice/store file per concern.
