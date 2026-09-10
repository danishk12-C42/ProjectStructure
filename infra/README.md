# infra/

Everything about running and deploying the product.

- `docker-compose.yml` → full local stack (SQL Server + backend + frontend)
- `azure/` → Azure infrastructure-as-code (Bicep). Deploy targets:
  - Backend → Azure App Service / Container Apps
  - Frontend → Azure Static Web Apps (or App Service)
  - Database → Azure SQL Database
  - Secrets → Azure Key Vault (referenced from App Service settings)

Rules:
- Infrastructure changes go through PR review like any code (see CODEOWNERS).
- No credentials in any file here — use Key Vault / GitHub environment secrets.
