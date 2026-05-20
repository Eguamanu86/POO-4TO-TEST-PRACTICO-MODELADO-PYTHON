# 🛒 Caso de Estudio 03: Inventario de Tienda Escolar

## Información General

| Campo | Detalle |
|------|---------|
| Asignatura | Programación Orientada a Objetos |
| Duración | 20 minutos |
| Nivel | Básico |
| Herramientas | Python 3.10+, editor de texto/IDE |

## Contexto
La librería escolar vende útiles y necesita controlar el stock disponible. Cuando se recibe mercancía se aumenta el inventario; cuando se despacha un producto, se reduce la cantidad. El sistema debe rechazar cambios que dejen el stock negativo.

## Objetivo
Diseñar y programar un modelo orientado a objetos para manejar productos y su inventario.

## Estructura de directorios sugerida
- `modelo/`
  - `producto.py`
  - `inventario.py`
- `uml/`
  - `caso_06_inventario.puml`
- `main.py`

## 1. Análisis / Abstracción

### Narrativa
- Cada producto tiene código, nombre, precio y cantidad disponible.
- El inventario almacena los productos disponibles.
- Se pueden agregar productos nuevos y actualizar las cantidades.
- Si no hay stock para una operación, la actualización debe rechazarse.

### Tareas de análisis
- Identifica entidades y atributos.
- Define qué responsabilidades tiene cada clase.
- Decide qué operaciones son necesarias para el inventario.

### Entidades sugeridas
- `Producto` → código, nombre, precio, stock
- `Inventario` → lista de productos

## 2. Diseño / Modelado de clases

### Relaciones
- `Inventario` contiene objetos `Producto`.
- `Producto` conoce su propio stock.

### Clases mínimas
- `Producto`
- `Inventario`

### Métodos propuestos
- `Producto.hay_stock(cantidad)`
- `Producto.modificar_stock(cantidad)`
- `Inventario.agregar_producto(producto)`
- `Inventario.actualizar_stock(codigo, cantidad)`
- `Inventario.consultar_stock(codigo)`

## 3. Implementación en Python

### Requisitos mínimos
- Usa atributos privados y propiedades.
- Implementa la lógica de stock dentro de `Producto`.
- Modela las clases UML en PlanTUML antes de codificar.
- `Inventario` debe buscar productos por código.
- Evita que el stock sea negativo.

### `main.py` debe:
- agregar 3 productos,
- aumentar el stock de uno,
- reducir el stock de otro,
- mostrar el stock final de un producto.

### Preguntas de comprobación
- ¿Por qué es importante que `Producto` controle su propio stock?
- ¿Qué clase se encarga de almacenar la lista de productos?
- ¿Qué pasa si intento descontar más stock del disponible?

---

## Resultado esperado
Un programa Python que maneja productos e inventario con control de stock y evita cantidades negativas.
