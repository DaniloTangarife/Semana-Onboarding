"""Solicita dos números y una operación (+, -, *, /). Muestra el resultado y evita la división entre cero."""

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
op = input("Operación (+, -, *, /): ")

if op == "+":
    print(f"Resultado: {a + b}")
elif op == "-":
    print(f"Resultado: {a - b}")
elif op == "*":
    print(f"Resultado: {a * b}")
elif op == "/":
    if b != 0:
        print(f"Resultado: {a / b}")
    else:
        print("No se puede dividir entre cero.")
else:
    print("Operación no válida.")