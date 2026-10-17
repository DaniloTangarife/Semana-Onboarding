"""Solicita el precio de una compra:

$200.000 o más: 20 % de descuento.
$100.000 o más: 10 % de descuento.
Menos de $100.000: sin descuento.
Muestra el total a pagar."""

precio = float(input("Ingresa el precio de la compra: "))

if precio >= 200000:
    descuento = 0.20
elif precio >= 100000:
    descuento = 0.10
else:
    descuento = 0

total = precio - (precio * descuento)

print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"Total a pagar: ${total:,.2f}")