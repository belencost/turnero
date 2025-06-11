from turnero import Turnero

# Crear instancia del sistema de turnos
t = Turnero()

# Diccionario de opciones disponibles
opciones = {
    "CAJ": "Caja",
    "COM": "Atención personalizada",
    "REC": "Reclamos",
    "JOP": "Jubilaciones, pensiones, ANSES"
}

print("Bienvenido al Turnero del Banco")
print("Seleccione una opción ingresando el código (o escriba SALIR):")

# Menu
for codigo, nombre in opciones.items():
    print(f"{codigo} - {nombre}")

while True:
    eleccion = input("Ingrese tipo de turno: (CAJ, COM, REC, JOB)").strip().upper()
    if eleccion == "SALIR":
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    elif eleccion in opciones:
        turno = t.generar_turno(eleccion)
        print(f"Su turno para {opciones[eleccion]} es: {turno}")
    else:
        print("Opción no válida. Intente de nuevo.")
