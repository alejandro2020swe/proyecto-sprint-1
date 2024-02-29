import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

# Creación contenido de nuestra aplicación basada en Streamlit.
# Encabezado con texto
st.header("Análisis de Anuncios de Venta de Vehículos")

# Botón para mostrar u ocultar el histograma de condición vs. modelo
show_histogram_button = st.button("Histograma de Condición vs. Modelo")

# Checkbox para seleccionar el modelo del auto en el gráfico de dispersión
show_scatter_checkbox = st.checkbox("Gráfico de Dispersión de Precio vs. Año del Modelo por modelo del auto")

# Lista de modelos de automóviles
car_models = car_data['model'].unique()

# Función para construir el histograma de condición vs. modelo
def build_histogram():
    fig = px.histogram(car_data, x="model", color="condition", title="Histograma de Condición vs. Modelo")
    st.plotly_chart(fig, use_container_width=True)

# Función para construir el gráfico de dispersión de precio vs. año del modelo
def build_scatter():
    selected_model = st.selectbox("Seleccionar modelo de automóvil", car_models)
    filtered_data = car_data[car_data['model'] == selected_model]
    fig = px.scatter(filtered_data, x="model_year", y="price", title=f"Gráfico de Dispersión de Precio vs. Año del Modelo para {selected_model}")
    st.plotly_chart(fig, use_container_width=True)

# Verificación si se hace clic en el botón y mostrar el histograma
if show_histogram_button:
    build_histogram()

# Verificación si el checkbox está seleccionado y mostrar el gráfico de dispersión
if show_scatter_checkbox:
    build_scatter()