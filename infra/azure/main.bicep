// Azure infrastructure-as-code placeholder.
// Define here when ready to deploy: App Service plan + web apps (backend,
// frontend), Azure SQL Database, Key Vault, Application Insights.
// Deploy via: az deployment group create -g <rg> -f main.bicep
targetScope = 'resourceGroup'

@description('Environment name, e.g. dev, staging, prod')
param environment string = 'dev'

// resource appServicePlan 'Microsoft.Web/serverfarms@2023-12-01' = { ... }
// resource backendApp 'Microsoft.Web/sites@2023-12-01' = { ... }
// resource sqlServer 'Microsoft.Sql/servers@2023-08-01-preview' = { ... }
// resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = { ... }

output environmentName string = environment
