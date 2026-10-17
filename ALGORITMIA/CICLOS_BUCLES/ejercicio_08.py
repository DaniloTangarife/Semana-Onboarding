"""Pide la altura y dibuja el triángulo con ciclos anidados, sin usar "*" * n:"""

altura = int(input("Altura: "))

for fila in range(1, altura + 1):
    for columna in range(fila):
        print("*", end="")
    print()