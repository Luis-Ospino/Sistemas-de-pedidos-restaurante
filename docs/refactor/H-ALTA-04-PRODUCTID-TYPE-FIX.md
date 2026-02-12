# Refactor H-ALTA-04: Corrección de Inconsistencia de Tipo productId

**Fecha:** 12 de febrero de 2026  
**Hallazgo:** H-ALTA-04 - Contrato tipo `productId` inconsistente entre frontend y backend  
**Rama:** `feature/fix-productid-type-inconsistency`  
**Estado:** EN PROGRESO

---

## Problema Identificado

Existe una inconsistencia de tipos entre el frontend y el backend para el campo `productId`:

- **Frontend:** Usa `string` para `productId`
- **Backend:** Espera `Long` (número) para `productId`

### Evidencia del Problema

**Frontend (`src/api/contracts.ts`):**
```typescript
export type Product = {
  id: string  // ← String
  // ...
}

export type OrderItem = {
  productId: string  // ← String
  // ...
}

export type CreateOrderRequest = {
  items: Array<{ productId: string; quantity: number; note?: string }>  // ← String
}
```

**Backend (`OrderItemRequest.java`):**
```java
public class OrderItemRequest {
    @NotNull(message = "Product ID is required")
    private Long productId;  // ← Long (número)
    // ...
}
```

**Backend (`Product.java`):**
```java
@Entity
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;  // ← Long (número)
    // ...
}
```

### Impacto

1. **Errores 400 potenciales:** Cuando el frontend envía `productId` como string, el backend puede fallar al deserializar
2. **Conversiones ad-hoc:** Necesidad de conversiones manuales en el código
3. **Confusión en desarrollo:** Desarrolladores deben recordar hacer conversiones
4. **Riesgo de bugs:** Fácil olvidar la conversión y causar errores en producción

---

## Análisis de Deuda Técnica

### Causas Raíz

1. **Falta de contrato compartido:** No existe un schema compartido (OpenAPI/GraphQL) que garantice consistencia
2. **Desarrollo desacoplado:** Frontend y backend desarrollados sin validación cruzada de tipos
3. **Ausencia de validación en desarrollo:** No hay tests de integración que validen el contrato
4. **Decisión de diseño inconsistente:** No se estableció una convención clara para IDs

### Tipo de Deuda Técnica

- **Deuda de Diseño:** Inconsistencia en la definición del contrato API
- **Deuda de Calidad:** Falta de validación de contratos entre capas
- **Deuda de Documentación:** No hay especificación formal del API

### ¿Por qué ocurrió?

1. **Desarrollo MVP rápido:** Prioridad en funcionalidad sobre consistencia
2. **Falta de governance:** No hay proceso de revisión de contratos API
3. **Tooling inadecuado:** No se usa TypeScript generado desde backend o OpenAPI
4. **Testing insuficiente:** No hay tests end-to-end que validen el flujo completo

---

## Análisis de Patrones de Diseño

### ¿Se aplican patrones en la solución?

**SÍ - Adapter Pattern (implícito)**

Aunque no se implementa explícitamente, la solución sigue el concepto del patrón Adapter:

**Definición del Adapter Pattern:**
> Convierte la interfaz de una clase en otra interfaz que los clientes esperan. Permite que clases con interfaces incompatibles trabajen juntas.

**Aplicación en este caso:**
- **Interfaz incompatible:** Frontend usa `string`, Backend usa `Long`
- **Adaptación:** Estandarizar a un tipo común que ambos entiendan
- **Resultado:** Ambas capas hablan el mismo "idioma"

### Opciones de Solución

#### Opción 1: Frontend adapta a Backend (ELEGIDA) ✅

**Cambiar frontend de `string` a `number`**

**Ventajas:**
- Backend ya usa el tipo correcto (`Long` → número)
- Los IDs de base de datos son numéricos (IDENTITY)
- Más eficiente en serialización JSON
- Consistente con el modelo de datos real

**Desventajas:**
- Requiere cambios en múltiples archivos del frontend
- Puede romper localStorage existente (migración necesaria)

**Patrón aplicado:** Adapter Pattern (frontend se adapta al backend)

#### Opción 2: Backend adapta a Frontend

**Cambiar backend de `Long` a `String`**

**Ventajas:**
- Más flexible (puede manejar UUIDs en el futuro)
- Frontend no cambia

**Desventajas:**
- Requiere cambios en entidades JPA
- Menos eficiente en base de datos
- Inconsistente con el modelo actual (IDENTITY genera números)
- Más cambios en backend (entidades, DTOs, repositorios)

**Patrón aplicado:** Adapter Pattern (backend se adapta al frontend)

#### Opción 3: Capa de traducción explícita

**Crear un DTO Adapter explícito**

**Ventajas:**
- Separación clara de responsabilidades
- Fácil cambiar en el futuro

**Desventajas:**
- Complejidad innecesaria para este caso
- Overhead de mantenimiento

**Patrón aplicado:** Adapter Pattern (explícito)

---

## Solución Elegida: Opción 1 (Frontend adapta a Backend)

### Justificación

1. **Consistencia con el modelo de datos:** Los IDs en base de datos son numéricos
2. **Menor impacto:** Solo cambios en frontend (TypeScript)
3. **Mejor performance:** Números son más eficientes que strings en JSON
4. **Alineación con estándares:** REST APIs típicamente usan números para IDs autogenerados

### Patrón de Diseño Aplicado

**Adapter Pattern (Implícito)**

El frontend actúa como un "adapter" que se ajusta a la interfaz esperada por el backend:

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│  Frontend   │────────>│   Adapter    │────────>│   Backend   │
│  (Client)   │         │  (Frontend   │         │  (Service)  │
│             │         │   ajustado)  │         │             │
└─────────────┘         └──────────────┘         └─────────────┘
   Antes: string           Ahora: number            Espera: Long
```

**Implementación:**
- **Target Interface:** Backend espera `Long` (número)
- **Adaptee:** Frontend originalmente usa `string`
- **Adapter:** Frontend modificado para usar `number`
- **Client:** Componentes React que usan el cart store

---

## Cambios a Realizar

### 1. Contratos TypeScript (`src/api/contracts.ts`)

```typescript
// ANTES
export type Product = {
  id: string  // ❌
  // ...
}

export type OrderItem = {
  productId: string  // ❌
  // ...
}

// DESPUÉS
export type Product = {
  id: number  // ✅
  // ...
}

export type OrderItem = {
  productId: number  // ✅
  // ...
}
```

### 2. Cart Store (`src/store/cart.tsx`)

```typescript
// ANTES
export type CartItem = {
  productId: string  // ❌
  // ...
}

// DESPUÉS
export type CartItem = {
  productId: number  // ✅
  // ...
}
```

### 3. Componentes que usan productId

- `src/pages/client/CartPage.tsx`
- Cualquier otro componente que referencie `productId`

### 4. Migración de localStorage (opcional pero recomendado)

Agregar lógica de migración para convertir `productId` string a number en datos existentes.

---

## Plan de Implementación

### Fase 1: Actualizar Tipos ✅
1. Modificar `src/api/contracts.ts`
2. Modificar `src/store/cart.tsx`
3. Verificar compilación TypeScript

### Fase 2: Actualizar Componentes ✅
1. Revisar y actualizar componentes que usan `productId`
2. Verificar que no haya conversiones manuales innecesarias

### Fase 3: Migración de Datos ✅
1. Agregar lógica de migración en cart store
2. Convertir datos existentes en localStorage

### Fase 4: Testing ✅
1. Compilar frontend
2. Probar flujo completo: agregar al carrito → crear orden
3. Verificar que el backend reciba el tipo correcto

### Fase 5: Documentación ✅
1. Actualizar este documento con resultados
2. Commit y push de cambios

---

## Prevención Futura

### Recomendaciones

1. **Usar OpenAPI/Swagger:**
   - Definir contratos en OpenAPI
   - Generar tipos TypeScript desde OpenAPI
   - Garantiza consistencia automática

2. **Tests de Integración:**
   - Agregar tests que validen el contrato completo
   - Usar herramientas como Pact para contract testing

3. **Code Review:**
   - Revisar cambios en contratos API
   - Validar consistencia entre frontend y backend

4. **Documentación:**
   - Mantener documentación actualizada de APIs
   - Usar herramientas como Swagger UI

5. **Linting/Validation:**
   - Agregar reglas de linting para validar tipos
   - Usar herramientas como `tsc --noEmit` en CI/CD

---

## Métricas de Éxito

- ✅ Compilación TypeScript sin errores
- ✅ Flujo de creación de orden funcional
- ✅ Backend recibe `Long` correctamente
- ✅ No hay errores 400 por tipo incorrecto
- ✅ Datos de localStorage migrados correctamente

---

## Conclusión

Este refactor resuelve una inconsistencia crítica en el contrato API aplicando implícitamente el **Adapter Pattern**. El frontend se adapta a la interfaz esperada por el backend, eliminando la deuda técnica y previniendo errores en producción.

**Hallazgo H-ALTA-04:** EN RESOLUCIÓN 🔄

