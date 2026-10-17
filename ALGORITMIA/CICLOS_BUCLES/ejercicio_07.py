"""Secreto: 37. Pide intentos y responde “más alto” o “más bajo” hasta acertar. Muestra los intentos usados:"""

secreto = 37
intentos = 0

while True:
    num = int(input("Adivina el número: "))
    intentos += 1

    if num < secreto:
        print("Más alto")
    elif num > secreto:
        print("Más bajo")
    else:
        print(f"¡Correcto! {intentos} intentos")
        break