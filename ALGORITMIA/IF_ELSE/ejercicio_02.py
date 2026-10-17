"""Solicita dos números, calcula su suma y resta. Indica si la suma es mayor que 10."""

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

suma = a + b
resta = a - b

print(f"Suma: {suma}")
print(f"Resta: {resta}")

if suma > 10:
    print("La suma es mayor que 10.")
else:
    print("La suma no es mayor que 10.")

    