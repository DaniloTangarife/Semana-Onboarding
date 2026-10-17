"""Solicita el nombre y la edad de una persona. Muestra su nombre e indica si es mayor de edad."""

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print(f"{nombre} tiene {edad} años.")
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")