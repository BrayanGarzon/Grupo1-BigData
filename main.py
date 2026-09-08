









total_ventas = df["total_venta"].sum()

ventas_producto = df.groupby("producto")["precio"].sum()
producto_mayor = ventas_producto.idxmax()

ventas_ciudad = df.groupby("ciudad")["total_venta"].sum()
ciudad_mayor = ventas_ciudad.idxmax()

print("\nTotal vendido: $", total_ventas)
print("Producto con mayores ventas:", producto_mayor)
print("Ciudad con mayores ventas:", ciudad_mayor)

print("\n====================================")
print("          FIN DEL INFORME")
print("====================================")
