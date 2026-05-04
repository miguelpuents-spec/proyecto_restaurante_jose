import almacenamiento
import gestor_logica

def mostrar_menu():
    print("\n--- 🍴 SISTEMA DE RESERVAS: DON JOSÉ ---")
    print("1. Registrar nueva reserva")
    print("2. Ver todas las reservas")
    print("3. Buscar una reserva")
    print("4. Modificar una reserva")
    print("5. Cancelar/Eliminar reserva")
    print("6. Salir")
    return input("Seleccione una opción: ")

def iniciar_programa():
    # Cargar datos guardados previamente al arrancar
    reservas = almacenamiento.cargar_datos()
    print("💾 Datos cargados correctamente.")

    while True:
        opcion = mostrar_menu()

        # --- OPCIÓN 1: Registrar nueva reserva ---
        if opcion == "1":
            nombre = input("Nombre del cliente: ").strip()
            if not nombre:
                print("⚠️ El nombre no puede estar vacío.")
                continue
            try:
                cantidad = int(input("¿Cuántas personas?: "))
                if cantidad <= 0:
                    print("⚠️ La cantidad debe ser mayor a cero.")
                    continue
                hora = input("Hora de la reserva (ej: 20:30): ").strip()
                if not hora:
                    print("⚠️ La hora no puede estar vacía.")
                    continue
                exito, mensaje = gestor_logica.verificar_y_agregar(reservas, nombre, cantidad, hora)
                print(mensaje)
                if exito:
                    # Guardado automático tras cada operación
                    almacenamiento.guardar_datos(reservas)
            except ValueError:
                print("⚠️ Error: Ingrese un número válido para las personas.")

        # --- OPCIÓN 2: Ver todas las reservas ---
        elif opcion == "2":
            if not reservas:
                print("\nNo hay reservas anotadas.")
            else:
                print("\n--- LISTA ACTUAL DE CLIENTES ---")
                for i, r in enumerate(reservas, 1):
                    print(f"{i}. {r['nombre']} — {r['personas']} personas — {r['hora']}")
                print(f"\nOcupación total: {gestor_logica.obtener_ocupacion_total(reservas)}/50 personas")

        # --- OPCIÓN 3: Buscar una reserva específica ---
        elif opcion == "3":
            nombre_buscar = input("Nombre del cliente a buscar: ").strip()
            resultado = gestor_logica.buscar_por_nombre(reservas, nombre_buscar)
            if resultado:
                print(f"\n🔍 Reserva encontrada:")
                print(f"   Nombre  : {resultado['nombre']}")
                print(f"   Personas: {resultado['personas']}")
                print(f"   Hora    : {resultado['hora']}")
            else:
                print(f"❌ No se encontró ninguna reserva para '{nombre_buscar}'.")

        # --- OPCIÓN 4: Modificar una reserva ---
        elif opcion == "4":
            nombre_modificar = input("Nombre del cliente cuya reserva desea modificar: ").strip()
            resultado = gestor_logica.buscar_por_nombre(reservas, nombre_modificar)
            if not resultado:
                print(f"❌ No se encontró ninguna reserva para '{nombre_modificar}'.")
                continue
            print(f"\nReserva actual: {resultado['nombre']} — {resultado['personas']} personas — {resultado['hora']}")
            print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
            try:
                nuevo_nombre = input(f"Nuevo nombre [{resultado['nombre']}]: ").strip() or resultado['nombre']
                nueva_cantidad_str = input(f"Nueva cantidad de personas [{resultado['personas']}]: ").strip()
                nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str else resultado['personas']
                if nueva_cantidad <= 0:
                    print("⚠️ La cantidad debe ser mayor a cero.")
                    continue
                nueva_hora = input(f"Nueva hora [{resultado['hora']}]: ").strip() or resultado['hora']
                exito, mensaje = gestor_logica.modificar_reserva(
                    reservas, nombre_modificar, nuevo_nombre, nueva_cantidad, nueva_hora
                )
                print(mensaje)
                if exito:
                    # Guardado automático tras modificar
                    almacenamiento.guardar_datos(reservas)
            except ValueError:
                print("⚠️ Error: Ingrese un número válido para las personas.")

        # --- OPCIÓN 5: Cancelar/Eliminar reserva ---
        elif opcion == "5":
            nombre_eliminar = input("Nombre de la reserva a cancelar: ").strip()
            if gestor_logica.eliminar_por_nombre(reservas, nombre_eliminar):
                print(f"🗑️ La reserva de {nombre_eliminar} ha sido eliminada.")
                # Guardado automático tras eliminar
                almacenamiento.guardar_datos(reservas)
            else:
                print(f"❌ No se encontró ninguna reserva con el nombre '{nombre_eliminar}'.")

        # --- OPCIÓN 6: Salir ---
        elif opcion == "6":
            almacenamiento.guardar_datos(reservas)
            print("💾 Datos guardados. ¡Hasta mañana, Don José!")
            break

        else:
            print("⚠️ Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    iniciar_programa()
