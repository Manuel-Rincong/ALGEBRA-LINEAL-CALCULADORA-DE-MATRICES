import numpy as np

def mostrar_menu():
    print("\n=== CALCULADORA DE MATRICES ===")
    print("1. Suma de matrices")
    print("2. Resta de matrices")
    print("3. Multiplicación de matrices")
    print("4. Matriz inversa")
    print("5. Salir")

def leer_matriz(nombre):
    filas = int(input(f"Ingrese el número de filas de la matriz {nombre}: "))
    columnas = int(input(f"Ingrese el número de columnas de la matriz {nombre}: "))
    print(f"Ingrese los elementos de la matriz {nombre}:")
    matriz = []
    for i in range(filas):
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        matriz.append(fila)
    return np.array(matriz)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        A = leer_matriz("A")
        B = leer_matriz("B")
        if A.shape == B.shape:
            print("\nResultado de la suma:\n", A + B)
        else:
            print("Error: las matrices deben tener el mismo tamaño.")

    elif opcion == "2":
        A = leer_matriz("A")
        B = leer_matriz("B")
        if A.shape == B.shape:
            print("\nResultado de la resta:\n", A - B)
        else:
            print("Error: las matrices deben tener el mismo tamaño.")

    elif opcion == "3":
        A = leer_matriz("A")
        B = leer_matriz("B")
        if A.shape[1] == B.shape[0]:
            print("\nResultado de la multiplicación:\n", np.dot(A, B))
        else:
            print("Error: el número de columnas de A debe ser igual al número de filas de B.")

    elif opcion == "4":
        A = leer_matriz("A")
        if A.shape[0] == A.shape[1]:
            try:
                print("\nMatriz inversa:\n", np.linalg.inv(A))
            except np.linalg.LinAlgError:
                print("Error: la matriz no tiene inversa (es singular).")
        else:
            print("Error: la matriz debe ser cuadrada para tener inversa.")

    elif opcion == "5":
        print("Saliendo de la calculadora...")
        break

    else:
        print("Opción no válida, intenta nuevamente.")