"""
def guardar_productos(productos):
    with open("productos.json", "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)

def agregar_nuevo_producto(productos, nuevo_producto):
    productos.append(nuevo_producto)
    guardar_productos(productos)

def generar_nuevo_id(productos):
    if not productos:
        return 1
    return max(producto["id"] for producto in productos) + 1
"""