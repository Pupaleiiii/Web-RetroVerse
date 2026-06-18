import streamlit as st
from lógica import cargar_productos, buscar_producto

if "carrito" not in st.session_state:
    st.session_state.carrito = []

st.set_page_config(
    page_title="RetroVerse",
    page_icon="🕹️",
    layout="wide"
)

productos = cargar_productos()

opcion = st.sidebar.selectbox(
    "Menú",
    [
        "🏠 Inicio",
        "📦 Ver catálogo",
        "🔍 Buscar producto",
        "🛒 Carrito"
    ]
)

if opcion == "🏠 Inicio":
    st.title("RetroVerse!")
    st.subheader("Reviví la nostalgia con objetos vintage, coleccionables y tecnología retro.")
    st.write("""
    Bienvenido a RetroVerse, una tienda digital de objetos retro.
    
    Utilizá el menú de la izquierda para explorar el catálogo, buscar productos o ver el carrito.
    """)

elif opcion == "📦 Ver catálogo":
    st.header("Catálogo")
    
    for producto in productos:
        st.subheader(producto["nombre"])
        st.write(f"**Categoría:** {producto['categoria']}")
        st.write(f"**Marca/desarrollador:** {producto['marca/desarrollador']}")
        st.write(f"**Año:** {producto['año']}")
        st.write(f"**Precio:** ${producto['precio']}")
        st.write(f"**Estado:** {producto['estado']}")
        
        if st.button(
            "🛒 Agregar al carrito",
            key=f"agregar_{producto['id']}"
        ):
            st.session_state.carrito.append(producto)
            st.success(f"{producto['nombre']} agregado al carrito exitosamente.")

        st.write("---")

elif opcion == "🔍 Buscar producto":
    st.header("🔍 Buscar producto por ID")

    id_buscado = st.number_input(
        "Ingresá el ID del producto",
        min_value=1,
        step=1
    )

    producto_buscado = buscar_producto(productos, id_buscado)

    if producto_buscado is not None:
        st.success("Producto encontrado")

        st.subheader(producto_buscado["nombre"])
        st.write(f"**Categoría:** {producto_buscado['categoria']}")
        st.write(f"**Marca/desarrollador:** {producto_buscado['marca/desarrollador']}")
        st.write(f"**Año:** {producto_buscado['año']}")
        st.write(f"**Precio:** ${producto_buscado['precio']}")
        st.write(f"**Estado:** {producto_buscado['estado']}")
        st.write(f"**Stock:** {producto_buscado['stock']}")
        st.write(f"**Descripción:** {producto_buscado['descripcion']}")

        if st.button(
            "🛒 Agregar al carrito",
            key=f"agregar_{producto_buscado['id']}"
        ):
            st.session_state.carrito.append(producto_buscado)
            st.success(
                f"'{producto_buscado['nombre']}' fue agregado al carrito."
            )

    else:
        st.error("No existe un producto con ese ID.")

elif opcion == "🛒 Carrito":
    st.header("🛒 Carrito de compras")

    if not st.session_state.carrito:
        st.write("El carrito está vacío.")
    else:
        total = 0

        for producto in st.session_state.carrito:
            st.write(
                f"{producto['nombre']} - ${producto['precio']}"
            )
            total += producto["precio"]

        st.write("---")
        st.subheader(f"Total: ${total}")