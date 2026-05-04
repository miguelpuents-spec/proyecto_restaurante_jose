# Definimos la capacidad total del restaurante según el requerimiento
CAPACIDAD_MAXIMA = 50

def obtener_ocupacion_total(reservas):
    """Suma la cantidad de personas de todas las reservas actuales."""
    return sum(r['personas'] for r in reservas)

def verificar_y_agregar(reservas, nombre, cantidad, hora):
    """Valida si hay mesas libres antes de confirmar la reserva."""
    ocupacion_actual = obtener_ocupacion_total(reservas)

    if ocupacion_actual + cantidad <= CAPACIDAD_MAXIMA:
        reservas.append({
            "nombre": nombre,
            "personas": cantidad,
            "hora": hora
        })
        return True, f" Reserva confirmada para {nombre} a las {hora}."
    else:
        disponibles = CAPACIDAD_MAXIMA - ocupacion_actual
        return False, f" No hay espacio suficiente. Solo quedan {disponibles} lugares disponibles."

def buscar_por_nombre(reservas, nombre_cliente):
    """Busca y devuelve una reserva específica sin modificarla."""
    for r in reservas:
        if r['nombre'].lower() == nombre_cliente.lower():
            return r
    return None

def modificar_reserva(reservas, nombre_cliente, nuevo_nombre, nueva_cantidad, nueva_hora):
    """Busca una reserva por nombre y actualiza sus datos."""
    for r in reservas:
        if r['nombre'].lower() == nombre_cliente.lower():
            # Calculamos la ocupación sin contar la reserva que se va a modificar
            ocupacion_sin_esta = obtener_ocupacion_total(reservas) - r['personas']
            if ocupacion_sin_esta + nueva_cantidad > CAPACIDAD_MAXIMA:
                disponibles = CAPACIDAD_MAXIMA - ocupacion_sin_esta
                return False, f" No se puede modificar. Solo hay {disponibles} lugares disponibles."
            r['nombre'] = nuevo_nombre
            r['personas'] = nueva_cantidad
            r['hora'] = nueva_hora
            return True, f" Reserva actualizada correctamente para {nuevo_nombre} a las {nueva_hora}."
    return False, " No se encontró ninguna reserva con ese nombre."

def eliminar_por_nombre(reservas, nombre_cliente):
    """Busca y elimina una reserva específica."""
    for i, r in enumerate(reservas):
        if r['nombre'].lower() == nombre_cliente.lower():
            reservas.pop(i)
            return True
    return False
