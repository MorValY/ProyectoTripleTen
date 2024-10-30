import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos


st.markdown("<h1 style='color: black;'>Análisis de Datos de Vehículos</h1>", unsafe_allow_html=True) #Titulo, color y tamano


st.markdown("<h2 style='color: red;'>Visión General de los Datos</h2>", unsafe_allow_html=True)

if st.checkbox('Mostrar modelos más usados'):
    st.subheader("Modelos más usados")
    model_counts = car_data['model'].value_counts()
    st.write(model_counts.head(15))  # Muestra los 15 modelos más comunes

st.dataframe(car_data)#Tabla de datos generales


hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma 
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo 
    st.plotly_chart(fig, use_container_width=True)

