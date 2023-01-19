import streamlit as st
import pandas as pd
import joblib

st.title("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.header("Una neurona con una entrada y un peso")
    w = st.slider("w0", 0.0, 10.0, key='w0tab1')
    x = st.number_input("x0", key='x0tab1')
    
    if st.button("Calcular la salida", key='buttontab1'):
        ytab1 = x*w
        st.text(ytab1)
        
with tab2:
    st.header("Una neurona con dos entradas y dos pesos")
    col1, col2 = st.columns(2)
    with col1:
        w0 = st.slider("w0", 0.0, 10.0, key='w0tab2')
        x0 = st.number_input("x0", key='x0tab2')
   
    with col2:
        w1 = st.slider("w1", 0.0, 10.0, key='w1tab2')
        x1 = st.number_input("x1", key='x1tab2')

    if st.button("Calcular la salida", key='buttontab2'):
        ytab2 = w0*x0 + w1*x1
        st.text(ytab2)
with tab3:
    st.header("Una neurona con tres entradas y tres pesos y un sesgo")
    col1, col2, col3 = st.columns(3)
    with col1:
        w0 = st.slider("w0", 0.0, 10.0, key='w0tab3')
        x0 = st.number_input("x0", key='x0tab3')
    with col2:
        w1 = st.slider("w1", 0.0, 10.0, key='w1tab3')
        x1 = st.number_input("x1", key='x1tab3')
    with col3:
        w2 = st.slider("w2", 0.0, 10.0, key='w2tab3')
        x2 = st.number_input("x2", key='x2tab3')
    b = st.number_input("bias")

    if st.button("Calcular la salida", key='buttontab3'):
        ytab3 = x0*w0 + x1*w1 + x2*w2 + b
        st.text(ytab3)