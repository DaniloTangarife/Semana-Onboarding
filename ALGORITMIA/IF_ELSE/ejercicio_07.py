"""Solicita la edad de una persona e indica si puede ingresar a un evento para mayores de 18 años. Valida que la edad no sea negativa."""

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad inválida.")
elif edad >= 18:
    print("Puede ingresar al evento.")
else:
    print("No puede ingresar, es menor de edad.")