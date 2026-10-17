"""Solicita una nota de 0 a 100 e indica si el estudiante está aprobado (70 o más) o reprobado. Valida la nota."""

nota = float(input("Ingresa la nota de 0 a 100: "))

if nota < 0 or nota > 100:
    print("Nota inválida.")
elif nota >= 70:
    print("Aprobado.")
else:
    print("Reprobado.")