"""Con notas = [4.5, 2.8, 3.9, 3.0, 2.2] calcula el promedio y cuántos aprobaron (nota ≥ 3.0):"""

notas = [4.5, 2.8, 3.9, 3.0, 2.2]

suma = 0
aprobados = 0

for nota in notas:
    suma += nota
    if nota >= 3.0:
        aprobados += 1

promedio = suma / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Aprobados: {aprobados}")