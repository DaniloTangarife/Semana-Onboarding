"""El saldo inicial es 100000.
Un menú con while se repite hasta elegir 4 (Salir).
Opción 1 consulta el saldo, 2 deposita y 3 retira.
No permitas retirar más del saldo ni montos negativos.
Al salir, muestra cuántas operaciones exitosas se hicieron.
Extra: si la opción no está entre 1 y 4, muestra “Opción inválida”."""

saldo = 100000
operaciones_exitosas = 0

while True:
    print("\n--- CAJERO ---")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    op = input("Opción: ")

    if op == "1":
        print(f"Saldo actual: ${saldo:,.2f}")
        operaciones_exitosas += 1
    elif op == "2":
        monto = float(input("Monto a depositar: "))
        if monto <= 0:
            print("Monto inválido.")
        else:
            saldo += monto
            operaciones_exitosas += 1
            print(f"Depósito exitoso. Saldo: ${saldo:,.2f}")
    elif op == "3":
        monto = float(input("Monto a retirar: "))
        if monto <= 0:
            print("Monto inválido.")
        elif monto > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= monto
            operaciones_exitosas += 1
            print(f"Retiro exitoso. Saldo: ${saldo:,.2f}")
    elif op == "4":
        print(f"Operaciones exitosas: {operaciones_exitosas}")
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")