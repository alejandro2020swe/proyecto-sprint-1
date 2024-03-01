import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('corazon.csv')

# Configurar la aplicación Streamlit
st.title('Análisis de Datos de Enfermedades Cardíacas')
st.write('Esta aplicación analiza datos de enfermedades cardíacas.')

# Mostrar un encabezado con texto
st.header('Datos de la Enfermedad Cardíaca')

# Mostrar una descripción breve
st.write('Los datos contienen información sobre pacientes con enfermedades cardíacas.')



# Botón para abrir el histograma de edad
if st.button('Ver Histograma de Edad'):
    st.subheader('Histograma de Edad')
    fig_hist = px.histogram(df, x='Age', color='Sex', title='Distribución de Edad por Género')
    st.plotly_chart(fig_hist)

# Botón para abrir el gráfico de dispersión de colesterol vs. presión arterial en reposo
if st.button('Ver Gráfico de Dispersión de Colesterol vs. Presión Arterial en Reposo'):
    st.subheader('Gráfico de Dispersión de Colesterol vs. Presión Arterial en Reposo')
    fig_scatter = px.scatter(df, x='RestingBP', y='Cholesterol', color='ChestPainType', title='Colesterol vs. Presión Arterial en Reposo por Tipo de Dolor de Pecho')
    st.plotly_chart(fig_scatter)

# Botón para mostrar/ocultar los datos detallados
if st.checkbox('Mostrar/Ocultar Datos'):
    st.subheader('Datos Detallados')
    st.write(df)
