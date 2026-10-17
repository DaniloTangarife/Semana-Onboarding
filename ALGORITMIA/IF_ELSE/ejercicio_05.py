"""Solicita dos números e indica cuál es mayor o si son iguales."""

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if a > b:
    print(f"El mayor es {a}.")
elif b > a:
    print(f"El mayor es {b}.")
else:
    print("Son iguales.")