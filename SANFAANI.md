# SANFAANI operations platform

SANFAANI is an internal console for charging, workspace visits, customer records, inventory, sales, and receipts. Admins and staff use it to manage daily work.

## 01 | Why it was built
**The problem:** The business used separate manual records for charging sessions, workspace use, inventory, and payments. It was hard to see what was happening across the business.
**The decision:** We built one system where each action records the service, transaction, receipt, and history.
**The result:** The project became a working tool for users, payments, and access control.

## 02 | What it does
It brings daily operations into one place. Admins and staff use the system. Customers receive receipts, QR claim codes, and notifications.

> **Inventory note:**
> The code currently calculates stock units and inventory costs [ IMPLEMENTED ]. Retail value and potential margin are planned but are not yet implemented in the backend [ DESIGNED ].

### Technology stack
| Technology | Responsibility |
| --- | --- |
| React + Vite + TS + Tailwind + TanStack Query + Generated API Client | User interface |
| Node + Express + TS + Zod + Mongoose | Business logic and validation |
| MongoDB | Data Persistence |
| Supabase Auth | User identity and authentication |
| OpenAPI | API rules and contract |
| pdf-lib / qrcode | Receipt and claim generation |
| Web Push / WhatsApp | Notifications |
| Vercel (Frontend) / Render (Backend) | Hosting |
| pnpm | Monorepo workspace |

## 03 | Architecture
1. **Client and server boundary:** The React frontend cannot access the database. Requests go through Zod validation and role checks on the Express backend.
2. **Session and claim flow:** Checkout creates a one-time QR code, so a device cannot be collected twice.
3. **Notifications:** If the WhatsApp API fails ([ IMPLEMENTED, DEPENDS ON EXTERNAL CONFIG ]), the sale still goes through.
4. **Deployment layers:** Supabase Auth and MongoDB are separate from the API and frontend.
5. **Shared ledger:** Every module sends its events to the same transaction ledger.
6. **Audit trail:** Each action from sign-in to checkout creates an audit log that cannot be changed.

## 04 | What I learned
Building SANFAANI taught me the difference between authentication and authorization. A user can log in without having access to everything, so the backend checks staff and admin roles. I also learned to keep core transactions separate from secondary services. If WhatsApp goes down, it should not cancel a completed sale in the database.

Using OpenAPI first made it easier to connect the frontend and backend. I also learned to model money carefully: possible margin is different from actual profit. Zod validation, rate limits, and audit logs showed me how to build a system a business can trust.
