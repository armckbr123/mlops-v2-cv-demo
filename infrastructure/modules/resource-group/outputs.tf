output "resource_group_name" {
  value = var.create_resource_group
  ? azurerm_resource_group.adl_rg[0].name
  : data.azurerm_resource_group.existing.name
}

output "resource_group_location" {
  value = var.create_resource_group
  ? azurerm_resource_group.adl_rg[0].location
  : data.azurerm_resource_group.existing.location
}