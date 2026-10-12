# ==========================================
# SISTEMA BÁSICO DE CONTROL DE INVENTARIO
# ==========================================

# 1. LISTAS Y DICCIONARIOS: Guardamos nuestros productos y precios
inventario_productos = ["Camisas", "Pantalones", "Zapatos", "Gorras"]
precios_productos = [15.0, 30.0, 45.0, 10.0]


# 2. FUNCIONES (El acceso rápido): Una receta para calcular el total a pagar
def calcular_total(precio_unitario, cantidad):
  total = precio_unitario * cantidad
  return total


# 3. BUCLES Y CONDICIONALES: Menú interactivo que no se cierra solo
en_ejecucion = True

print("--- BIENVENIDO AL SISTEMA DE GESTIÓN ---")

while en_ejecucion:
  print("\n¿Qué deseas hacer?")
  print("1. Ver lista de productos")
  print("2. Simular una venta")
  print("3. Salir")

  opcion = input("Elige una opción (1, 2 o 3): ")

  # Condicionales para tomar decisiones según lo que elija el usuario
  if opcion == "1":
    print("\n--- PRODUCTOS DISPONIBLES ---")
    # Mostramos los productos usando un bucle simple
    for i in range(len(inventario_productos)):
      print(f"- {inventario_productos[i]} : ${precios_productos[i]}")

  elif opcion == "2":
    print("\n--- REGISTRAR VENTA ---")
    producto_elegido = input(
        "¿Qué producto quiere el cliente? (Camisas/Pantalones/Zapatos/Gorras): "
    )

    if producto_elegido in inventario_productos:
      # Buscamos la posición del producto en la lista
      posicion = inventario_productos.index(producto_elegido)
      precio = precios_productos[posicion]

      cantidad_str = input("¿Cuántas unidades se llevan?: ")
      cantidad = int(cantidad_str)

      # Llamamos a nuestra función de acceso rápido para calcular el costo
      costo_final = calcular_total(precio, cantidad)

      print(
          f"¡Venta registrada! Total a cobrar por {cantidad}"
          f" {producto_elegido}: ${costo_final}"
      )
    else:
      print("Lo siento, ese producto no existe en el inventario.")

  elif opcion == "3":
    print("Saliendo del sistema. ¡Hasta luego!")
    en_ejecucion = False  # Esto rompe el bucle while y termina el programa

  else:
    print("Opción no válida. Por favor elige 1, 2 o 3.")