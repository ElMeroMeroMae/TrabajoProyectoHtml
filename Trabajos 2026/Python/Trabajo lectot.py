import json

lista_ventas = []

try:
    with open("ventas.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:

            producto, cantidad = linea.strip().split(",")
            
            venta = {
                "producto": producto,
                "cantidad": int(cantidad) 
            }
            lista_ventas.append(venta)
            
    print("Archivo 'ventas.txt' leído correctamente.")
except FileNotFoundError:
    print("Error, No se encontró el archivo 'ventas.txt'. Crealo primero, prix.")
    exit()


totales_por_producto = {}


for registro in lista_ventas:
    prod = registro["producto"]
    cant = registro["cantidad"]
    
    if prod in totales_por_producto:
        totales_por_producto[prod] += cant
    else:
        totales_por_producto[prod] = cant


with open("resumen.json", "w", encoding="utf-8") as archivo_json:

    json.dump(totales_por_producto, archivo_json, indent=4, ensure_ascii=False)

print("✅ Resultados consolidados y guardados en 'resumen.json'.")

producto_mas_vendido = max(totales_por_producto, key=totales_por_producto.get)
total_maximo = totales_por_producto[producto_mas_vendido]

print("\n--- REPORTE EN PANTALLA ---")
print(f"El producto más vendido es: {producto_mas_vendido} con un total de {total_maximo} unidades.")