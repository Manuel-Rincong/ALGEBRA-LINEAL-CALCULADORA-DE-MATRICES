import streamlit as st
import numpy as np

# Configuración básica de la página
st.set_page_config(page_title="Calculadora de Matrices", page_icon="🔢", layout="wide")

st.title("🔢 Calculadora de Matrices")
st.markdown("### Realiza operaciones con matrices fácilmente")
st.write("---")

# Función para crear matriz usando entradas dinámicas
def crear_matriz(nombre, filas_default=2, columnas_default=2):
    st.subheader(f"Matriz {nombre}")
    col1, col2 = st.columns(2)
    with col1:
        filas = st.number_input(f"Filas de Matriz {nombre}", min_value=1, max_value=10, value=filas_default, key=f"filas_{nombre}")
    with col2:
        columnas = st.number_input(f"Columnas de Matriz {nombre}", min_value=1, max_value=10, value=columnas_default, key=f"columnas_{nombre}")

    st.write(f"Ingrese los valores para {nombre} ({int(filas)}x{int(columnas)}):")

    matriz = []
    for i in range(int(filas)):
        fila = []
        cols = st.columns(int(columnas))
        for j in range(int(columnas)):
            with cols[j]:
                valor = st.number_input(f"[{i},{j}]", value=0.0, key=f"{nombre}_{i}_{j}", label_visibility="collapsed")
                fila.append(valor)
        matriz.append(fila)
    return np.array(matriz)

# Funciones de cálculo
def suma_matrices(a, b):
    if a.shape != b.shape:
        return None, "Las matrices deben tener las mismas dimensiones"
    return a + b, None

def resta_matrices(a, b):
    if a.shape != b.shape:
        return None, "Las matrices deben tener las mismas dimensiones"
    return a - b, None

def multiplicar_matrices(a, b):
    if a.shape[1] != b.shape[0]:
        return None, "Columnas de A deben igualar filas de B"
    return np.dot(a, b), None

def determinante_matriz(a):
    if a.shape[0] != a.shape[1]:
        return None, "La matriz debe ser cuadrada"
    return np.linalg.det(a), None

def inversa_matriz(a):
    if a.shape[0] != a.shape[1]:
        return None, "La matriz debe ser cuadrada"
    det = np.linalg.det(a)
    if abs(det) < 1e-10:
        return None, "La matriz no tiene inversa (determinante = 0)"
    return np.linalg.inv(a), None

def transpuesta_matriz(a):
    return np.transpose(a), None

def traza_matriz(a):
    if a.shape[0] != a.shape[1]:
        return None, "La matriz debe ser cuadrada"
    return np.trace(a), None

def escalar_matriz(a, esc):
    return a * esc, None

# Menú lateral y operación
st.sidebar.title("⚙️ Opciones")
operacion = st.sidebar.selectbox(
    "Selecciona la operación:",
    [
        "Suma", "Resta", "Multiplicación", "Determinante", "Inversa",
        "Transpuesta", "Traza", "Escalar"
    ]
)

st.write("## Entrada de Datos")

if operacion in ["Suma", "Resta", "Multiplicación"]:
    col1, col2 = st.columns(2)
    with col1:
        matriz_a = crear_matriz("A")
    with col2:
        matriz_b = crear_matriz("B")
else:
    matriz_a = crear_matriz("A")

# Si la operación es escalar, pedir el número escalar antes de presionar el botón
if operacion == "Escalar":
    escalar = st.number_input("Número escalar por el que multiplicar la matriz A", value=1.0)

if st.button("Calcular", type="primary"):
    try:
        if operacion == "Suma":
            resultado, error = suma_matrices(matriz_a, matriz_b)
        elif operacion == "Resta":
            resultado, error = resta_matrices(matriz_a, matriz_b)
        elif operacion == "Multiplicación":
            resultado, error = multiplicar_matrices(matriz_a, matriz_b)
        elif operacion == "Determinante":
            resultado, error = determinante_matriz(matriz_a)
        elif operacion == "Inversa":
            resultado, error = inversa_matriz(matriz_a)
        elif operacion == "Transpuesta":
            resultado, error = transpuesta_matriz(matriz_a)
        elif operacion == "Traza":
            resultado, error = traza_matriz(matriz_a)
        elif operacion == "Escalar":
            resultado, error = escalar_matriz(matriz_a, escalar)
        else:
            resultado, error = None, "Operación no soportada"

        if error:
            st.error(f"❌ {error}")
        else:
            st.success("✅ Operación realizada correctamente")
            st.write("### Resultado:")
            st.write(resultado)
    except Exception as e:
        st.error(f"❌ Error inesperado: {str(e)}")

st.write("---")
st.info("💡 Usa la barra lateral para cambiar de operación. Ingresa los valores y presiona 'Calcular'.")

st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "<strong>Calculadora de Matrices</strong><br>"
    "Desarrollado por estudiantes.<br>"
    "Tecnologías: Python 🐍 | Streamlit 🎈 | NumPy 🔢"
    "</div>", unsafe_allow_html=True
)