"""
elif opcion == "➕ Agregar nuevo producto":
    st.header("Agregar nuevo producto")
    
    id = generar_nuevo_id(productos)
    nombre = st.text_input("Nombre")
    categoria = st.text_input("Categoría")
    marca = st.text_input("Marca")
    año = st.number_input("Año", min_value=1900, max_value=2026)
    estado = st.selectbox("Estado", ["Nuevo", "Usado", "Restaurado"])
    precio = st.number_input("Precio", min_value=0.00)
    stock = st.number_input("Stock", min_value=0, step=1)
    descripcion = st.text_area("Descripción")

    if st.button("Agregar producto"):
        nuevo_producto = {
            "id": id,
            "nombre": nombre,
            "categoria": categoria,
            "marca": marca,
            "año": año,
            "estado": estado,
            "precio": precio,
            "stock": stock,
            "descripcion": descripcion
        }
        agregar_nuevo_producto(productos, nuevo_producto)
        st.success("Producto agregado correctamente")

elif opcion == "Modificar producto":
    st.header("Modificar producto")
    # Mostrar formulario

elif opcion == "🗑️ Eliminar producto":
    st.header("Eliminar producto")
    # Mostrar formulario
"""