# Archivo: 04_proyecto_automatizador.py
# Proyecto Real: Simulador de script para automatizar la entrega de reportes a clientes.

import os

def crear_reporte_cliente(nombre_cliente, datos):
    """
    Función que crea una carpeta y un archivo de texto con un reporte formateado.
    Esto es exactamente lo que un negocio paga por automatizar.
    """
    # 1. Definimos el nombre de la carpeta
    nombre_carpeta = f"cliente_{nombre_cliente.lower()}"
    
    # 2. Creamos la carpeta (si no existe)
    os.makedirs(nombre_carpeta, exist_ok=True)
    
    # 3. Ruta del archivo final
    ruta_archivo = os.path.join(nombre_carpeta, "reporte_financiero.txt")
    
    # 4. Escribimos los datos dentro del archivo
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(f"=== REPORTE OFICIAL PARA: {nombre_cliente.upper()} ===\n")
        archivo.write("Estado del servicio: Automatizado con Python\n")
        archivo.write("Datos procesados:\n")
        
        # Usamos un bucle para escribir cada dato de la lista
        for item in datos:
            archivo.write(f" - {item}\n")
            
    print(f"[ÉXITO] Carpeta '{nombre_carpeta}' y reporte creados correctamente.")

# --- SIMULACIÓN DEL SERVICIO FREELANCE ---
if __name__ == "__main__":
    print("--- SISTEMA AUTOMATIZADO DE CLIENTES ---")
    
    # Supongamos que estos son los datos que nos mandó un cliente
    cliente_actual = "TechSolutions"
    datos_recibidos = ["Ventas Enero: $1500", "Ventas Febrero: $2300", "Ventas Marzo: $1900"]
    
    # Llamamos a nuestra función principal
    crear_reporte_cliente(cliente_actual, datos_recibidos)