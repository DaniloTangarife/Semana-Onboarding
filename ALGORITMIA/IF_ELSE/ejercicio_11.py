"""Solicita una temperatura y clasifícala:

Menos de 10 °C: frío.
De 10 a menos de 25 °C: templado.
De 25 a menos de 35 °C: caluroso.
35 °C o más: muy caluroso."""

temperatura = float(input("Ingresa la temperatura en °C: "))

if temperatura < 10:
    print("Frío.")
elif temperatura < 25:
    print("Templado.")
elif temperatura < 35:
    print("Caluroso.")
else:
    print("Muy caluroso.")