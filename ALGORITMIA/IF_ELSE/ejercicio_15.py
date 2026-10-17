"""Solicita el nombre del cliente, el producto, su precio y la cantidad. Calcula el subtotal y aplica estos descuentos:

$500.000 o más: 15 %.
$200.000 o más: 10 %.
Menos de $200.000: sin descuento.
Muestra una factura con el subtotal, el descuento y el total a pagar."""

cliente = input("Nombre del cliente: ")
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad

if subtotal >= 500000:
    descuento_porcentaje = 0.15
elif subtotal >= 200000:
    descuento_porcentaje = 0.10
else:
    descuento_porcentaje = 0

descuento = subtotal * descuento_porcentaje
total = subtotal - descuento

print("\n--- FACTURA ---")
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio:,.2f}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Descuento ({descuento_porcentaje * 100:.0f}%): ${descuento:,.2f}")
print(f"Total a pagar: ${total:,.2f}")