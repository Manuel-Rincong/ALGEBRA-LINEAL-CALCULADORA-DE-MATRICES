import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Calculadora de Matrices", page_icon="🧮", layout="centered")

st.title("🧮 Calculadora de Matrices")
st.markdown("---")
st.subheader("1. Operaciones con una matriz.")
st.markdown("---")
st.title("MATRIZ X.")
st.subheader("Configura el tamaño de la matriz.")
st.markdown("---")

colX1, colX2 = st.columns(2)
filasX = colX1.number_input("Numero de Filas",min_value=1, max_value=10, value=3, key="Filas X")
columnasX = colX2.number_input("Numero de Columnas",min_value=1, max_value=10, value=3, key="Columnas X")

if "matrizX" not in st.session_state:
    st.session_state.matrizX = pd.DataFrame(np.zeros((filasX,columnasX)))

if st.session_state.matrizX.shape != (filasX, columnasX):
    st.session_state.matrizX = pd.DataFrame(np.zeros((filasX, columnasX)))

st.session_state.matrizX = st.data_editor(st.session_state.matrizX, key="X", num_rows="fixed")

X = st.session_state.matrizX.to_numpy()
resultadoX = None

st.subheader("Operaciones.")
col1,col2,col3,col4 = st.columns(4)

with col1:
    if st.button("Determinante"):
        if X.shape[0] == X.shape[1]:
            resultadoX = np.linalg.det(X)
        else:
            st.error("La matriz debe ser cuadrada.")

with col2:
    if st.button("Inversa"):
        if X.shape[0] == X.shape[1]:
            try:
                resultado = np.linalg.inv(X)
            except np.linalg.LinAlgError:
                st.error("La matriz X no tiene inversa (es singular).")
        else:
            st.error("La matriz debe ser cuadrada.")

with col3:
    if st.button("Traspuesta"):
        resultadoX = np.transpose(X)

with col4:
    if st.button("Traza"):
        if X.shape[0] == X.shape[1]:
            resultadoX = np.trace(X)
        else:
            st.error("La matriz debe ser cuadrada.")











st.subheader("Configura los tamaños de las matrices.")
st.markdown("---")

# ==============================
# CONFIGURACIÓN DE MATRIZ A
# ==============================
st.subheader("Matriz A")

colA1, colA2 = st.columns(2)
filasA = colA1.number_input("Numero de Filas", min_value=1, max_value=10, value=3, )
columnasA = colA2.number_input("Numero de Columnas", min_value=1, max_value=10, value=3)

# Inicialización en session_state
if "matrizA" not in st.session_state:
    st.session_state.matrizA = pd.DataFrame(np.zeros((filasA, columnasA)))

# Si cambia el tamaño, reiniciar matriz
if st.session_state.matrizA.shape != (filasA, columnasA):
    st.session_state.matrizA = pd.DataFrame(np.zeros((filasA, columnasA)))

st.session_state.matrizA = st.data_editor(st.session_state.matrizA, key="A", num_rows="fixed")

# ==============================
# CONFIGURACIÓN DE MATRIZ B
# ==============================
st.subheader("Matriz B")

colB1, colB2 = st.columns(2)
filasB = colB1.number_input("Filas de B", min_value=1, max_value=10, value=3)
columnasB = colB2.number_input("Columnas de B", min_value=1, max_value=10, value=3)

if "matrizB" not in st.session_state:
    st.session_state.matrizB = pd.DataFrame(np.zeros((filasB, columnasB)))

if st.session_state.matrizB.shape != (filasB, columnasB):
    st.session_state.matrizB = pd.DataFrame(np.zeros((filasB, columnasB)))

st.session_state.matrizB = st.data_editor(st.session_state.matrizB, key="B", num_rows="fixed")

# ==============================
# CONVERTIR A NUMPY
# ==============================
A = st.session_state.matrizA.to_numpy()
B = st.session_state.matrizB.to_numpy()
resultado = None

# ==============================
# OPERACIONES
# ==============================
st.subheader("⚙️ Operaciones")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("➕ Sumar"):
        if A.shape == B.shape:
            resultado = A + B
        else:
            st.error("❌ Las matrices deben tener el mismo tamaño para sumarse.")

with col2:
    if st.button("➖ Restar"):
        if A.shape == B.shape:
            resultado = A - B
        else:
            st.error("❌ Las matrices deben tener el mismo tamaño para restarse.")

with col3:
    if st.button("✖️ Multiplicar"):
        if A.shape[1] == B.shape[0]:
            resultado = np.dot(A, B)
        else:
            st.error("❌ Las columnas de A deben coincidir con las filas de B.")

with col4:
    if st.button("🔄 Inversa de A"):
        if A.shape[0] == A.shape[1]:
            try:
                resultado = np.linalg.inv(A)
            except np.linalg.LinAlgError:
                st.error("❌ La matriz A no tiene inversa (es singular).")
        else:
            st.error("❌ A debe ser cuadrada para calcular su inversa.")

# ==============================
# RESULTADO
# ==============================
if resultado is not None:
    st.subheader("✅ Resultado:")
    st.dataframe(pd.DataFrame(resultado))
