import json

def cargar_productos():
    with open("productos.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)
    
def buscar_producto(productos, id_buscado):
    for producto in productos:
        if producto["id"] == id_buscado:
            return producto    
    return None

