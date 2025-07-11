<h1 style="color:#009979;"> AgroVerde grupo 1</h1>

**Desafío:** AE5_ABPRO-Ejercicio grupal [Actividad Opcional]  
**Integrantes:** 
- David Ferrer
- Jasmin Salvador
- Patricia Vidal
- Abraham Lillo

---

## 📋 Descripción

AgroVerde es un programa en Python diseñado para optimizar la gestión de un pequeño emprendimiento de productos agrícolas orgánicos. Facilita la organización de inventario, el registro de clientes y el seguimiento de pedidos de forma interactiva y validada.

---
## 🚦 Flujos de uso

A continuación se describen los principales flujos de interacción con el sistema:

### 1. Agregar un producto
1. En el menú principal, seleccionar “Agregar producto”.  
2. Ingresar el nombre del producto (no vacío).  
3. Ingresar la categoría del producto (no vacío).  
4. Confirmación de agregado y retorno al menú.

### 2. Eliminar un producto
1. En el menú, seleccionar “Eliminar producto”.  
2. Se muestra el inventario numerado.  
3. Ingresar el número correspondiente al producto a eliminar.  
4. El sistema valida el índice y, si es correcto, elimina el producto y actualiza categorías.  
5. Mensaje de confirmación y regreso al menú.

### 3. Registrar un cliente
1. En el menú, elegir “Agregar cliente”.  
2. Ingresar nombre, teléfono y dirección (todos obligatorios).  
3. Validaciones de campos no vacíos; en caso de error, se repite el ingreso.  
4. Cliente guardado con ID único.  
5. Mensaje de éxito y vuelta al menú.

### 4. Crear un pedido
1. En el menú, seleccionar “Registrar pedido”.  
2. Si hay clientes registrados:  
   - Mostrar listado de clientes y pedir un ID.  
   - Si el usuario no ingresa ID válido, se crean datos de un nuevo cliente.  
3. Si no hay clientes, se solicita crear uno nuevo.  
4. Mostrar inventario numerado.  
5. Ingresar los números de productos separados por comas.  
6. Validar cada índice; ignorar inválidos.  
7. Guardar el pedido con lista de productos y estado “pendiente”.  
8. Mostrar mensaje con ID de pedido y conteo de productos.

### 5. Actualizar estado de un pedido
1. En el menú, seleccionar “Actualizar estado”.  
2. Mostrar lista de pedidos con su ID y estado actual.  
3. Ingresar el ID del pedido a modificar.  
4. Ingresar nuevo estado (pendiente, procesado o entregado).  
5. Validar estado y actualizar en la estructura.  
6. Confirmación y retorno al menú.

---