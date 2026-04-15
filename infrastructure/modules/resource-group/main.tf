resource "azurerm_resource_group" "adl_rg" {
  count    = var.create_resource_group ? 1 : 0
  name     = "rg-${var.prefix}-${var.postfix}${var.env}"
  location = var.location
  tags     = var.tags
}