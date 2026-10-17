"""Crea un cajero con un saldo inicial de $500.000 y estas opciones:

Consultar saldo.
Retirar dinero.
Depositar dinero.
Salir.
Valida las operaciones y actualiza el saldo."""

saldo = 500000

while True:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    op = input("Selecciona una opción: ")

    if op == "1":
        print(f"Saldo actual: ${saldo:,.2f}")
    elif op == "2":
        monto = float(input("Monto a retirar: "))
        if monto <= 0:
            print("Monto inválido.")
        elif monto > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:,.2f}")
    elif op == "3":
        monto = float(input("Monto a depositar: "))
        if monto <= 0:
            print("Monto inválido.")
        else:
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:,.2f}")
    elif op == "4":
        print("Saliendo del cajero...")
        break
    else:
        print("Opción inválida.")