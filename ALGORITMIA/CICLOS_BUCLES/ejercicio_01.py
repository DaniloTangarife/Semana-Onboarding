"""Pide un número con input() y muestra la cuenta regresiva hasta 1; al final, “¡Despegue!”. Usa while. """

n = int(input("Número: "))

while n >= 1:
    print(n, end=" ")
    n -= 1

print("¡Despegue!")