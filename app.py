import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos


st.markdown("<h1 style='color: black;'>Análisis de Datos de Vehículos</h1>", unsafe_allow_html=True) #Titulo, color y tamano


st.markdown("<h2 style='color: red;'>Visión General de los Datos</h2>", unsafe_allow_html=True)

if st.checkbox('Mostrar modelos más vendidos'):
    st.subheader("Modelos más vendidos")
    model_counts = car_data['model'].value_counts()
    st.write(model_counts.head(15))  # Muestra los 15 modelos más comunes

st.dataframe(car_data)#Tabla de datos generales


hist_button = st.button('Datos de anuncios de venta') # crear un botón

if hist_button: # al hacer clic en el botón # escribir un mensaje
    st.write('Histograma que muestra el conjunto de datos de anuncios de venta de coches')
    # crear un histograma 
    fig = px.histogram(car_data, x="odometer", color_discrete_sequence=["orange"])
    # mostrar un gráfico Plotly interactivo 
    st.plotly_chart(fig, use_container_width=True)


# Botón para construir un histograma de condition vs model_year
hist_button = st.button('Condición vs Año del Modelo')

if hist_button:  # al hacer clic en el botón
    st.write('Histograma que muestra la relación entre la condición del vehiculo y el año del modelo')
    
    # Crear el histograma
    fig = px.histogram(
        car_data,
        x="model_year",
        color="condition",
        title="Histograma de Condición vs Año del Modelo",
        barmode='overlay'  # Las barras se superponen
    )
    # Mostrar el gráfico Plotly interactivo 
    st.plotly_chart(fig, use_container_width=True)


price_condition_button = st.button('Precio vs Condición')

if price_condition_button:  # al hacer clic en el botón
    st.write('Grafica de dispersión de Precio vs Condición de los vehiculos')
    
    # Crear el gráfico de dispersión
    fig_price_condition = px.scatter(
        car_data,
        x="price",          # Eje X
        y="condition",      # Eje Y
        color="condition",  # Color según la condición
        title="Gráfico de Dispersión de Precio vs Condición",
        labels={"price": "Precio ($)", "condition": "Condición"}
    )
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_price_condition, use_container_width=True)
