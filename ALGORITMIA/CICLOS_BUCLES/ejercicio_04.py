"""Pide un texto y cuenta cuántas vocales tiene, sin importar si están en mayúscula o minúscula:"""

texto = input("Texto: ").lower()
vocales = 0

for letra in texto:
    if letra in "aeiou":
        vocales += 1

print(f"Vocales: {vocales}")