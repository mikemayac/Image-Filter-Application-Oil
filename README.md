# Aplicación de Filtro de Óleo

### Joel Miguel Maya Castrejón │ mike.maya@ciencias.unam.mx │ 417112602

Esta aplicación web fue creada con **Python** y **Streamlit** que permite aplicar un **filtro de Óleo** a una imagen digital, recreando un efecto de pintura al óleo.  
Para ello, utilizamos una **convolución** de 7x7 (por defecto) alrededor de cada píxel, seleccionando el valor de gris más frecuente en dicho vecindario y asignándolo al píxel resultante (en su versión básica para imágenes en blanco y negro). En la demo actual, la conversión se hace sobre la imagen convertida a escala de grises y finalmente se regresa a RGB para mostrarla y descargarla.

---

## Requisitos

- Python 3.12 o superior.
- [Streamlit](https://docs.streamlit.io/) para la creación de la interfaz web.
- [Pillow](https://pillow.readthedocs.io/) (PIL) para la manipulación de imágenes.

En el archivo **requirements.txt** se listan las dependencias necesarias. Asegúrate de instalarlas antes de ejecutar la aplicación.

---

## Instalación

1. [**Clona** este repositorio](https://github.com/mikemayac/Image-Filter-Application-Oil) en tu máquina local.
2. Crea y activa un **entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # En Windows: venv\Scripts\activate
   ```
3. Instala los paquetes necesarios:
   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecución de la Aplicación

1. Dentro del entorno virtual, ubícate en la carpeta donde se encuentra el archivo principal (por ejemplo, `oleo.py`).
2. Ejecuta:
   ```bash
   streamlit run oleo.py
   ```
3. Automáticamente se abrirá tu navegador mostrando la interfaz de la aplicación.  
   Si no se abre, copia la URL que aparece en la terminal y pégala en tu navegador.

---

## Uso de la Aplicación

1. **Sube una imagen** en la barra lateral (sidebar), en formatos `JPG`, `JPEG` o `PNG`.  
2. Ajusta el **tamaño de la ventana** para el filtro de Óleo (por defecto 7x7).  
3. **Observa** cómo se muestra la **imagen original** en una columna y la **imagen resultante** en la otra columna.  
4. **Descarga** la imagen procesada haciendo clic en el botón de descarga que aparece sobre la imagen resultante.

---

## Estructura del Proyecto

```bash
.
├── oleo.py                # Código principal de la aplicación 
├── .streamlit/            # Carpeta de configuración de Streamlit 
│    └── config.toml       # Configuraciones extra de Streamlit
├── README.md              # Archivo de documentación
├── requirements.txt       # Dependencias del proyecto (Streamlit, Pillow, etc.)
└── venv/                  # Entorno virtual 
```

