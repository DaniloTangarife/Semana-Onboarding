"""Solicita un usuario y una contraseña. Compara los datos con valores definidos y permite el acceso si ambos coinciden."""

usuario_correcto = "admin"
clave_correcta = "1234"

usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == usuario_correcto and clave == clave_correcta:
    print("Acceso permitido.")
else:
    print("Acceso denegado.")