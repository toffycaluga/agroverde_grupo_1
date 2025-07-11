# AgroVerde_grupoX.py

# Estructuras de datos globales
inventario=[
    {'nombre':'tomate', 'categoria': 'hortalizas'},
    {'nombre':'manzana', 'categoria': 'frutas'},
    {'nombre':'lechuga', 'categoria': 'hortalizas'},
]

categorias = { item['categoria'] for item in inventario }
clientes = {}
siguiente_cliente_id = 1
pedidos = {}
siguiente_pedido_id = 1

# Función para leer un entero con validación
def leer_entero(prompt):
    texto = input(prompt).strip()
    if not texto.isdigit():
        print("❌ Entrada inválida; se esperaba un número.")
        return None
    return int(texto)

# Gestión de inventario
def agregar_producto():
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return

    categoria = input("Categoría: ").strip()
    if not categoria:
        print("❌ La categoría no puede estar vacía.")
        return

    inventario.append({"nombre": nombre, "categoria": categoria})
    categorias.add(categoria)
    print(f"✅ Producto '{nombre}' agregado en categoría '{categoria}'.")


def mostrar_inventario():
    if not inventario:
        print("— Inventario vacío —")
        return

    print("\nInventario disponible:")
    for i, item in enumerate(inventario, 1):
        print(f" {i}. {item['nombre']} ({item['categoria']})")
    print(f"Total productos: {len(inventario)}")
    print(f"Categorías: {', '.join(sorted(categorias))}")


def eliminar_producto():
    mostrar_inventario()
    idx = leer_entero("Número de producto a eliminar: ")
    if idx is None:
        return
    if idx < 1 or idx > len(inventario):
        print("❌ Índice fuera de rango.")
        return

    eliminado = inventario.pop(idx-1)
    if all(item["categoria"] != eliminado["categoria"] for item in inventario):
        categorias.discard(eliminado["categoria"])

    print(f"🗑️ Producto '{eliminado['nombre']}' eliminado.")

# Gestión de clientes
def crear_cliente():
    nombre = input("Nombre cliente: ").strip()
    telefono = input("Teléfono: +56").strip()
    direccion= input("Dirección: ").strip()
    if not (nombre and telefono and direccion):
        print("❌ Todos los campos son obligatorios.")
        return None
    return (nombre, telefono, direccion)


def agregar_cliente():
    global siguiente_cliente_id
    cliente = crear_cliente()
    if not cliente:
            # Si hubo error, devolvemos None
        return None  

    # cid = cliente_id
    cid = siguiente_cliente_id
    clientes[cid] = cliente
    print(f"✅ Cliente #{cid} registrado: {cliente[0]}")
    siguiente_cliente_id += 1
    # Devolvemos el ID recién creado
    return cid          


def mostrar_clientes():
    if not clientes:
        print("— No hay clientes dados de alta —")
        return

    print("\nClientes registrados:")
    # cid = cliente_id | n = nombre | t = telefono | d = direccion
    for cid, (n, t, d) in clientes.items():
        print(f" {cid}. {n} | {t} | {d}")

# Gestión de pedidos
def registrar_pedido():
    global siguiente_pedido_id

    # 1) Seleccionar o crear cliente
    if clientes:
        mostrar_clientes()
        opc = input("ID de cliente (o Enter para nuevo): ").strip()
        if opc.isdigit() and int(opc) in clientes:
            cliente = clientes[int(opc)]
        else:
            print("Creando nuevo cliente...")
            nuevo_id = agregar_cliente()  
            if not nuevo_id:
                return
            cliente = clientes[nuevo_id] 
    else:
        print("No hay clientes. Creando uno nuevo...")
        nuevo_id = agregar_cliente()  
        if not nuevo_id:
            return
        cliente = clientes[nuevo_id] 

    # 2) Seleccionar productos
    mostrar_inventario()
    entrada = input("Ingresa números de productos (coma): ").strip()
    if not entrada:
        print("❌ No ingresaste productos.")
        return

    indices = []
    for parte in entrada.split(","):
        if parte.strip().isdigit():
            idx = int(parte.strip())
            if 1 <= idx <= len(inventario):
                indices.append(idx-1)
            else:
                print(f"⚠️ Índice {idx} ignorado (fuera de rango).")
        else:
            print(f"⚠️ '{parte}' no es un número; ignorado.")

    if not indices:
        print("❌ No hay productos válidos para el pedido.")
        return

    productos = [inventario[i]["nombre"] for i in indices]

    # 3) Guardar pedido
    pedidos[siguiente_pedido_id] = {
        "cliente": cliente,
        "productos": productos,
        "estado": "pendiente"
    }
    print(f"🆔 Pedido #{siguiente_pedido_id} con {len(productos)} productos registrado.")
    siguiente_pedido_id += 1


def mostrar_pedidos():
    if not pedidos:
        print("— No hay pedidos —")
        return

    print("\nPedidos:")
    for pid, info in pedidos.items():
        nombre = info["cliente"][0]
        print(f" {pid}. Cliente: {nombre} | Productos: {len(info['productos'])} | Estado: {info['estado']}")


def actualizar_estado():
    mostrar_pedidos()
    # pid = pedido id
    pid = leer_entero("ID de pedido a actualizar: ")
    if pid is None or pid not in pedidos:
        print("❌ Pedido no encontrado.")
        return

    nuevo = input("Nuevo estado (pendiente/procesado/entregado): ").strip().lower()
    if nuevo not in ("pendiente", "procesado", "entregado"):
        print("❌ Estado inválido.")
        return

    pedidos[pid]["estado"] = nuevo
    print(f"✅ Pedido #{pid} ahora '{nuevo}'.")

# Menú principal
def menu():
    opciones = {
        "1": ("Mostrar inventario", mostrar_inventario),
        "2": ("Agregar producto",    agregar_producto),
        "3": ("Eliminar producto",   eliminar_producto),
        "4": ("Agregar cliente",     agregar_cliente),
        "5": ("Mostrar clientes",    mostrar_clientes),
        "6": ("Registrar pedido",    registrar_pedido),
        "7": ("Ver pedidos",         mostrar_pedidos),
        "8": ("Actualizar estado",   actualizar_estado),
        "0": ("Salir",               exit)
    }

    while True:
        print("\n==== Menu AgroVerde ====")
        for k, (desc, _) in opciones.items():
            print(f"[{k}] {desc}")
        sel = input("Opción: ").strip()
        if sel in opciones:
            opciones[sel][1]()
        else:
            print("❌ Opción inválida, intenta de nuevo.")

menu()
