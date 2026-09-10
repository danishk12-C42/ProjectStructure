# src/pages/

One file per route/page. Pages are thin: they compose feature components and
layouts — no business logic here.

Example: `OrdersPage.tsx` renders `<OrdersList />` from `features/orders/`
inside a layout from `layouts/`.
