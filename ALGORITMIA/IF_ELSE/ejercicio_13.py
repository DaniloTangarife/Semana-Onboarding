"""Crea un menú con las opciones de sumar, restar, multiplicar y dividir. Ejecuta la operación seleccionada y muestra el resultado."""

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

op = input("Selecciona una opción (1-4): ")

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if op == "1":
    print(f"Resultado: {a + b}")
elif op == "2":
    print(f"Resultado: {a - b}")
elif op == "3":
    print(f"Resultado: {a * b}")
elif op == "4":
    if b != 0:
        print(f"Resultado: {a / b}")
    else:
        print("No se puede dividir entre cero.")
else:
    print("Opción inválida.")