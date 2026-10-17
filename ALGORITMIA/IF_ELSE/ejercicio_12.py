"""Solicita los tres lados de un triángulo. Comprueba si es válido y clasifícalo como equilátero, isósceles o escaleno."""

a = float(input("Ingresa el lado 1: "))
b = float(input("Ingresa el lado 2: "))
c = float(input("Ingresa el lado 3: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("El triángulo no es válido.")
else:
    if a == b == c:
        print("Es equilátero.")
    elif a == b or a == c or b == c:
        print("Es isósceles.")
    else:
        print("Es escaleno.")