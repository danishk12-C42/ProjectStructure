# Git Workflow

We use **trunk-based development with short-lived branches**. `main` is always
deployable and protected.

## Rules

1. **Never commit directly to `main`.** Enable branch protection:
   require a PR, at least 1 approving review, and passing CI checks.
2. **Branches are short-lived** — merge within 1–3 days. Small PRs review
   faster and conflict less.
3. **Update from `main` daily** while your branch is open:
   `git fetch origin && git rebase origin/main` (or merge if rebase is uncomfortable).
4. **Squash-merge** PRs — keeps `main` history clean: one commit per PR.

## Branch naming

```
feature/<ticket-id>-short-description    e.g. feature/PRJ-12-login-page
fix/<ticket-id>-short-description        e.g. fix/PRJ-40-null-order-total
chore/<short-description>                e.g. chore/upgrade-ruff
```

## Commit messages — Conventional Commits

```
<type>(<scope>): <summary>

feat(orders): add order cancellation endpoint
fix(auth): refresh token expiry off by one hour
chore(ci): cache pip dependencies
docs(api): document pagination convention
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`.

## Avoiding merge conflicts (why our setup works)

| Practice | Effect |
|---|---|
| Feature-based folders | Different features = different files = no overlap |
| Auto-formatting via pre-commit/husky | No formatting-diff conflicts |
| `.gitattributes` LF normalization | No line-ending conflicts across OSes |
| Small, frequent PRs | Conflicts stay tiny and easy to resolve |
| Daily rebase on `main` | You resolve drift early, not at merge time |

## Pull request flow

1. Create branch from latest `main`.
2. Commit (pre-commit hooks auto-format).
3. Push and open a PR — the template checklist appears automatically.
4. CI runs (only the pipelines for the part you changed, thanks to path filters).
5. CODEOWNERS are auto-requested for review.
6. Address review comments, then **squash-merge**. Delete the branch.

## Database migrations

- One migration per PR maximum, generated with
  `alembic revision --autogenerate -m "add orders table"`.
- Migrations are append-only: never edit a migration that reached `main`.
- If two PRs create migrations simultaneously, the second author reruns
  `alembic merge` / regenerates on rebase.
