import streamlit as st
from PIL import Image
from io import BytesIO

# Configuración de la página
st.set_page_config(page_title="Filtro de Óleo", layout="wide")


def aplicar_filtro_oleo(imagen, window_size=7):
    """
    Aplica un filtro de 'Óleo digital' a la imagen.
    El algoritmo toma un vecindario (window_size x window_size)
    alrededor de cada píxel (en escala de grises),
    y asigna al píxel resultante el valor de gris más frecuente
    en dicho vecindario.

    Parámetros:
    -----------
    imagen: PIL.Image
        Imagen de entrada, en RGB o cualquier modo compatible.
    window_size: int
        Tamaño de la ventana (ej. 7 implica un vecindario de 7x7).
        Debe ser un número impar para tener un píxel central bien definido.

    Retorna:
    --------
    PIL.Image (RGB) con el filtro aplicado.
    """
    # Convertir a escala de grises para simplificar el histograma.
    # Cada píxel tendrá un valor 0..255.
    gray_image = imagen.convert("L")
    width, height = gray_image.size

    # Creamos la imagen de salida, inicialmente en escala de grises.
    output_gray = Image.new("L", (width, height))

    # Cargar pixeles para acceso rápido
    input_pixels = gray_image.load()
    output_pixels = output_gray.load()

    # Definir un "offset" para recorrer el vecindario alrededor de cada píxel
    offset = window_size // 2

    for y in range(height):
        for x in range(width):
            # Arreglo para el histograma de 256 posibles valores de gris
            histogram = [0] * 256

            # Recorrer el vecindario (window_size x window_size)
            for dy in range(-offset, offset + 1):
                for dx in range(-offset, offset + 1):
                    nx = x + dx
                    ny = y + dy

                    # Verificar que no nos salgamos de la imagen
                    if 0 <= nx < width and 0 <= ny < height:
                        valor_gris = input_pixels[nx, ny]  # 0..255
                        histogram[valor_gris] += 1

            # Encontrar el tono de gris con la mayor frecuencia
            max_valor_gris = max(range(256), key=lambda i: histogram[i])

            # Asignar ese valor al píxel de salida
            output_pixels[x, y] = max_valor_gris

    # Convertir el resultado a RGB para poder mostrarlo sin problemas en Streamlit
    resultado_final = output_gray.convert("RGB")
    return resultado_final


def main():
    st.sidebar.title("Configuraciones")

    # Único "filtro" disponible es el de Óleo
    st.sidebar.markdown("### Filtro activo: Óleo Digital")
    window_size = st.sidebar.slider("Tamaño de la ventana (para el efecto)", 3, 11, 7, step=2)
    uploaded_file = st.sidebar.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    imagen_resultante = None
    buf_value = None

    if uploaded_file is not None:
        # Cargamos la imagen original
        imagen_original = Image.open(uploaded_file).convert("RGB")

        # Aplicar el filtro de Óleo
        with st.spinner("Aplicando el filtro de Óleo..."):
            imagen_resultante = aplicar_filtro_oleo(imagen_original, window_size=window_size)

        # Preparar la imagen para descarga
        buf = BytesIO()
        imagen_resultante.save(buf, format="PNG")
        buf_value = buf.getvalue()

    # Crear la fila del título con el botón de descarga
    title_col, button_col = st.columns([4, 1])

    with title_col:
        st.title("Filtro de Óleo Digital")

    with button_col:
        if imagen_resultante is not None and buf_value is not None:
            st.download_button(
                label="⬇️ Descargar imagen",
                data=buf_value,
                file_name="imagen_oleo.png",
                mime="image/png",
                key="download_button_top"
            )

    # Mostrar las imágenes si se subió un archivo
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.image(imagen_original, caption="Imagen Original", use_container_width=True)
        with col2:
            st.image(imagen_resultante, caption="Imagen con Filtro de Óleo", use_container_width=True)
    else:
        st.info("Sube una imagen para ver el efecto de Óleo Digital.")


if __name__ == "__main__":
    main()
