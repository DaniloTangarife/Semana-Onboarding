"""Pide n y muestra la suma de todos los números de 1 a n. Usa for, range() y un acumulador: """

n = int(input("Número: "))
suma = 0

for i in range(1, n + 1):
    suma += i

print(f"La suma es {suma}")