import pandas as pd
import plotly.express as px
import streamlit as st

data = pd.read_csv('corazon.csv')

# Configurar la aplicación Streamlit
st.title('Análisis de Datos de Enfermedades Cardíacas')
st.write('Esta aplicación analiza datos de enfermedades cardíacas.')

# Mostrar un encabezado con texto
st.header('Datos de la Enfermedad Cardíaca')

# Mostrar una descripción breve
st.write('Los datos contienen información sobre pacientes con enfermedades cardíacas.')

# Mostrar los datos cargados
st.subheader('Datos')
st.write(data)

# Mostrar un histograma de la edad
st.subheader('Histograma de Edad')
fig_hist = px.histogram(data, x='Age', title='Distribución de Edad')
st.plotly_chart(fig_hist)

# Mostrar un gráfico de dispersión de colesterol vs. presión arterial en reposo
st.subheader('Gráfico de Dispersión de Colesterol vs. Presión Arterial en Reposo')
fig_scatter = px.scatter(data, x='RestingBP', y='Cholesterol', color='HeartDisease', title='Colesterol vs. Presión Arterial en Reposo')
st.plotly_chart(fig_scatter)

# Agregar un botón de casilla de verificación para mostrar/ocultar los datos
if st.checkbox('Mostrar/Ocultar Datos'):
    st.subheader('Datos Detallados')
    st.write(data)