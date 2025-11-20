##Instalar las librerias, escribir en la terminal "pip install streamlit"
#Para ejecutar el codigo escribir en la terminal "streamlit run Codigos/prueba4.py"

import streamlit as st

#Funciones 
#----------------------------- Funciones Para Crear Las Matrices -----------------------------

#Funcion Para Crear Una Matriz Con Listas
def crear_matriz(filas, columnas, valor=0.0):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(valor)
        matriz.append(fila)
    return matriz

#Funcion Para Crear Una Copia De La Matriz 
def copiar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    copia = crear_matriz(filas, columnas)
    for i in range(filas):
        for j in range(columnas):
            copia[i][j] = matriz[i][j]
    return copia

#----------------------------- Funciones Para Calcular Operaciones Con Una Matriz -----------------------------

#Funcion Para Calcular El Determinante De Una Matriz
def determinante(matriz):
    n = len(matriz)
    m = copiar_matriz(matriz)
    det = 1.0
    
    for i in range(n):
        # Buscar el pivote máximo
        max_fila = i
        for k in range(i + 1, n):
            if abs(m[k][i]) > abs(m[max_fila][i]):
                max_fila = k
        
        # Intercambiar filas si es necesario
        if max_fila != i:
            m[i], m[max_fila] = m[max_fila], m[i]
            det = -det
        
        # Si el pivote es 0, el determinante es 0
        if abs(m[i][i]) < 1e-10:
            return 0.0
        
        det = det * m[i][i]
        
        # Eliminación gaussiana
        for k in range(i + 1, n):
            factor = m[k][i] / m[i][i]
            for j in range(i, n):
                m[k][j] = m[k][j] - factor * m[i][j]
    
    return det

#Funcion Para Calcular La Inversa De Una Matriz
def matriz_inversa(matriz):
    n = len(matriz)
    # Crear matriz aumentada [A|I]
    aumentada = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(float(matriz[i][j]))
        for j in range(n):
            if i == j:
                fila.append(1.0)
            else:
                fila.append(0.0)
        aumentada.append(fila)
    
    # Eliminación gaussiana hacia adelante
    for i in range(n):
        # Buscar pivote
        max_fila = i
        for k in range(i + 1, n):
            if abs(aumentada[k][i]) > abs(aumentada[max_fila][i]):
                max_fila = k
        
        aumentada[i], aumentada[max_fila] = aumentada[max_fila], aumentada[i]
        
        # Verificar si la matriz es singular
        if abs(aumentada[i][i]) < 1e-10:
            return None
        
        # Dividir la fila por el pivote
        pivote = aumentada[i][i]
        for j in range(2 * n):
            aumentada[i][j] = aumentada[i][j] / pivote
        
        # Eliminación
        for k in range(n):
            if k != i:
                factor = aumentada[k][i]
                for j in range(2 * n):
                    aumentada[k][j] = aumentada[k][j] - factor * aumentada[i][j]
    
    # Extraer la matriz inversa
    inversa = crear_matriz(n, n)
    for i in range(n):
        for j in range(n):
            inversa[i][j] = aumentada[i][j + n]
    
    return inversa

#Funcion Para Calcular La Transpuesta De Una Matriz 
def transpuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    trans = crear_matriz(columnas, filas)
    for i in range(filas):
        for j in range(columnas):
            trans[j][i] = matriz[i][j]
    return trans

#Funcion Para Calcular La Traza De Una Matriz
def traza(matriz):
    n = len(matriz)
    suma = 0.0
    for i in range(n):
        suma = suma + matriz[i][i]
    return suma

#----------------------------- Funciones Para Calcular Operaciones Con Dos Matrices -----------------------------

#Funcion Para Calcular La Suma De Matrices
def sumar_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    resultado = crear_matriz(filas, columnas)
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = A[i][j] + B[i][j]
    return resultado

#Funcion Para Calcular La Resta De Matrices
def restar_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    resultado = crear_matriz(filas, columnas)
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = A[i][j] - B[i][j]
    return resultado

#Funcion Para Calcular La Multiplicacion De Matrices
def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])
    resultado = crear_matriz(filas_A, columnas_B)
    for i in range(filas_A):
        for j in range(columnas_B):
            suma = 0.0
            for k in range(columnas_A):
                suma = suma + A[i][k] * B[k][j]
            resultado[i][j] = suma
    return resultado

#----------------------------- Funcion Para La Visualizacion De La Matriz -----------------------------

#Convierte La Matriz A Tabla HTML Para Mostrar En Streamlit
def matriz_a_tabla_html(matriz):
    html = "<table style='border-collapse: collapse; margin: 10px auto;'>"
    for fila in matriz:
        html += "<tr>"
        for valor in fila:
            html += f"<td style='border: 1px solid #ddd; padding: 8px; text-align: center;'>{valor:.2f}</td>"
        html += "</tr>"
    html += "</table>"
    return html

#----------------------------- Configuracion De Streamlit -----------------------------

st.set_page_config(page_title="Calculadora de Matrices", page_icon="🧮", layout="centered")

st.title("🧮 Calculadora de Matrices")
st.markdown("---")

#----------------------------- Seccion 1 De La Interfaz Web -----------------------------

st.title("1. Operaciones Con Una Matriz")
st.markdown("---")
st.title("MATRIZ X")
st.subheader("Configure el tamaño de la matriz")
st.markdown("---")

colX1, colX2 = st.columns(2)
filasX = colX1.number_input("Número de Filas", min_value=1, max_value=10, value=3, key="FilasX")
columnasX = colX2.number_input("Número de Columnas", min_value=1, max_value=10, value=3, key="ColumnasX")

# Inicializar matriz X en session_state
if "matrizX" not in st.session_state:
    st.session_state.matrizX = crear_matriz(filasX, columnasX)

# Redimensionar si cambia el tamaño
if len(st.session_state.matrizX) != filasX or len(st.session_state.matrizX[0]) != columnasX:
    st.session_state.matrizX = crear_matriz(filasX, columnasX)

# Editor de matriz X
st.markdown("**Ingrese los valores de la matriz:**")
for i in range(filasX):
    cols = st.columns(columnasX)
    for j in range(columnasX):
        with cols[j]:
            st.session_state.matrizX[i][j] = st.number_input(
                f"X[{i},{j}]",
                value=float(st.session_state.matrizX[i][j]),
                step=1.0,
                key=f"X_{i}_{j}",
                label_visibility="collapsed"
            )

X = st.session_state.matrizX
resultadoX = None

st.markdown("---")
st.subheader("Operaciones")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Determinante"):
        if filasX == columnasX:
            resultadoX = determinante(X)
        else:
            st.error("La matriz debe ser cuadrada")

with col2:
    if st.button("Inversa"):
        if filasX == columnasX:
            inv = matriz_inversa(X)
            if inv is None:
                st.error("La matriz no tiene inversa (es singular)")
            else:
                resultadoX = inv
        else:
            st.error("La matriz debe ser cuadrada")

with col3:
    if st.button("Transpuesta"):
        resultadoX = transpuesta(X)

with col4:
    if st.button("Traza"):
        if filasX == columnasX:
            resultadoX = traza(X)
        else:
            st.error("La matriz debe ser cuadrada")

st.markdown("---")
if resultadoX is not None:
    if isinstance(resultadoX, (int, float)):
        st.write(f"**Resultado: {resultadoX}**")
    else:
        st.markdown("**Resultado:**")
        st.markdown(matriz_a_tabla_html(resultadoX), unsafe_allow_html=True)

#----------------------------- Seccion 2 De La Interfaz Web -----------------------------

st.markdown("---")
st.title("2. Operaciones Entre 2 Matrices")
st.markdown("---")

st.title("MATRIZ A")
st.subheader("Configure el tamaño de la matriz A")
st.markdown("---")

colA1, colA2 = st.columns(2)
filasA = colA1.number_input("Número de Filas", min_value=1, max_value=10, value=3, key="FilasA")
columnasA = colA2.number_input("Número de Columnas", min_value=1, max_value=10, value=3, key="ColumnasA")

if "matrizA" not in st.session_state:
    st.session_state.matrizA = crear_matriz(filasA, columnasA)

if len(st.session_state.matrizA) != filasA or len(st.session_state.matrizA[0]) != columnasA:
    st.session_state.matrizA = crear_matriz(filasA, columnasA)

st.markdown("**Ingrese los valores de la matriz A:**")
for i in range(filasA):
    cols = st.columns(columnasA)
    for j in range(columnasA):
        with cols[j]:
            st.session_state.matrizA[i][j] = st.number_input(
                f"A[{i},{j}]",
                value=float(st.session_state.matrizA[i][j]),
                step=1.0,
                key=f"A_{i}_{j}",
                label_visibility="collapsed"
            )

st.markdown("---")
st.title("MATRIZ B")
st.subheader("Configure el tamaño de la matriz B")
st.markdown("---")

colB1, colB2 = st.columns(2)
filasB = colB1.number_input("Filas de B", min_value=1, max_value=10, value=3, key="FilasB")
columnasB = colB2.number_input("Columnas de B", min_value=1, max_value=10, value=3, key="ColumnasB")

if "matrizB" not in st.session_state:
    st.session_state.matrizB = crear_matriz(filasB, columnasB)

if len(st.session_state.matrizB) != filasB or len(st.session_state.matrizB[0]) != columnasB:
    st.session_state.matrizB = crear_matriz(filasB, columnasB)

st.markdown("**Ingrese los valores de la matriz B:**")
for i in range(filasB):
    cols = st.columns(columnasB)
    for j in range(columnasB):
        with cols[j]:
            st.session_state.matrizB[i][j] = st.number_input(
                f"B[{i},{j}]",
                value=float(st.session_state.matrizB[i][j]),
                step=1.0,
                key=f"B_{i}_{j}",
                label_visibility="collapsed"
            )

A = st.session_state.matrizA
B = st.session_state.matrizB
resultado = None

st.markdown("---")
st.subheader("Operaciones")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Sumar"):
        if filasA == filasB and columnasA == columnasB:
            resultado = sumar_matrices(A, B)
        else:
            st.error("Las matrices deben tener el mismo tamaño")

with col2:
    if st.button("Restar"):
        if filasA == filasB and columnasA == columnasB:
            resultado = restar_matrices(A, B)
        else:
            st.error("Las matrices deben tener el mismo tamaño")

with col3:
    if st.button("Multiplicar"):
        if columnasA == filasB:
            resultado = multiplicar_matrices(A, B)
        else:
            st.error("Las columnas de A deben coincidir con las filas de B")

st.markdown("---")
if resultado is not None:
    st.markdown("**Resultado:**")
    st.markdown(matriz_a_tabla_html(resultado), unsafe_allow_html=True)