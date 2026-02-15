import type { OrderItem, Product } from '@/api/contracts'

export function buildProductNameMap(products: Product[] | undefined): Map<string, string> {
  const map = new Map<string, string>()
  for (const product of products ?? []) {
    if (product.name) map.set(product.id, product.name)
  }
  return map
}

export function resolveOrderItemName(item: OrderItem, productNames: Map<string, string>): string {
  const explicitName = item.name?.trim()
  if (explicitName) return explicitName
  return productNames.get(item.productId) ?? `Producto ${item.productId}`
}

