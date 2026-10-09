def calcular_duracion(hora_1, hora_2):
    return hora_2 - hora_1
#Ejecuta una resta para determinar el tiempo total transcurrido


def calcular_porcentaje_dia(duracion_correcta):
    return int(duracion_correcta / 24 * 100)
#Realiza una division seguida de una multiplicacion para calcular el porcentaje del dia usado


def generar_resumen(dia, duracion, porcentaje):
    return dia, duracion, porcentaje
#Genera un resumen en base a los datos obtenidos previamente


def formato_hora(hora_1, hora_2):
    hora_programada_i = ((hora_1 - 1) % 12) + 1
    hora_programada_f = ((hora_2 - 1) % 12) + 1
    if hora_1 < 12 or hora_1 == 24:
        momento_i = "AM"
    else:
        momento_i = "PM"
    if hora_2 < 12 or hora_2 == 24:
        momento_f = "AM"
    else:
        momento_f = "PM"
    return hora_programada_i, momento_i, "a", hora_programada_f, momento_f
#Acomoda las horas ingresadas (0 a 24) al formato de AM/PM por medio de una resta, seguido de su residuo al dividirse entre 12


def horas_validas(hora_1, hora_2):
    if hora_2 > hora_1:
        return "Horas validas"
    else:
        return "Ingrese horas validas"
#Compara horas ingresadas para determinar si son posibles o irreales


def calcular_horas_libres(horas_usadas):
    return 24 - horas_usadas
#Ejecuta una resta para determinar las horas libres restantes


def momento_dia(hora_usada):
    parte_dia = int(hora_usada // 6) % 4
    if parte_dia == 0:
        return "Break of day"
    elif parte_dia == 1:
        return "Morning"
    elif parte_dia == 2:
        return "Afternoon"
    else:
        return "Night"
#Por medio de una division entera de la hora entre 6 y su residuo entre 4 para determinar en que momento del dia cae la hora


def leer_opcion(mensaje, opcion_1, opcion_2):
    opcion = input(mensaje)
    while opcion != opcion_1 and opcion != opcion_2:
        opcion = input("Ingresa una opcion valida: ")
    return opcion
#Pide una opcion hasta que sea una de las dos permitidas


def leer_hora(mensaje):
    hora = float(input(mensaje))
    while hora < 0 or hora > 24:
        hora = float(input("La hora debe estar entre 0 y 24: "))
    return hora
#Pide una hora hasta que esta este entre 0 y 24 (que sea valida)


def mostrar_bloque(nombre, dia, hora_inicio, hora_final, duracion, porcentaje):
    print("Tu", nombre, "abarca:", formato_hora(hora_inicio, hora_final))
    print("Duracion:", duracion, "hrs/hr")
    print("Porcentaje del dia usado:", porcentaje, "%")
    print("Resumen (Dia/Duracion/Uso):", generar_resumen(dia, duracion, porcentaje))
    print("Horario valido?:", horas_validas(hora_inicio, hora_final))
    print("Momento del dia en que inicia:", momento_dia(hora_inicio))
    print("Momento del dia en que termina:", momento_dia(hora_final))
#Imprime los resultados de un bloque de tiempo en base a lo registrado por el usuario


def programar_ocupada():
    dia = input("Escribe el dia que quieres programar: ")
    total_ocupado = 0
    seguir = "Si"
    while total_ocupado < 24 and seguir == "Si":
        hora_inicio_actividad = leer_hora("Inicio actividad: ")
        hora_final_actividad = leer_hora("Final actividad: ")
        while horas_validas(hora_inicio_actividad, hora_final_actividad) != "Horas validas" or total_ocupado + calcular_duracion(hora_inicio_actividad, hora_final_actividad) > 24:
            print("Ingrese horas validas, la actividad no puede pasar de 24 hrs en total")
            hora_inicio_actividad = leer_hora("Inicio actividad: ")
            hora_final_actividad = leer_hora("Final actividad: ")
        duracion_actividad = calcular_duracion(hora_inicio_actividad, hora_final_actividad)
        total_ocupado = total_ocupado + duracion_actividad
        porcentaje_dia = calcular_porcentaje_dia(total_ocupado)
        mostrar_bloque("actividad", dia, hora_inicio_actividad, hora_final_actividad, duracion_actividad, porcentaje_dia)
        print("Horas libres restantes:", calcular_horas_libres(total_ocupado))
        if total_ocupado < 24:
            seguir = leer_opcion("Agregar otra actividad? Si o No: ", "Si", "No")
#Agrega actividades del dia hasta que el usuario quiera reminar o se completen las 24 hrs


def programar_libre():
    dia_libre = input("Escribe el dia que quieres programar: ")
    hora_inicio_tiempo_libre = leer_hora("Inicio de tiempo libre: ")
    hora_final_tiempo_libre = leer_hora("Final de tiempo libre: ")
    while horas_validas(hora_inicio_tiempo_libre, hora_final_tiempo_libre) != "Horas validas":
        print("Ingrese horas validas")
        hora_inicio_tiempo_libre = leer_hora("Inicio de tiempo libre: ")
        hora_final_tiempo_libre = leer_hora("Final de tiempo libre: ")
    duracion_tiempo_libre = calcular_duracion(hora_inicio_tiempo_libre, hora_final_tiempo_libre)
    porcentaje_dia_libre = calcular_porcentaje_dia(duracion_tiempo_libre)
    mostrar_bloque("descanso", dia_libre, hora_inicio_tiempo_libre, hora_final_tiempo_libre, duracion_tiempo_libre, porcentaje_dia_libre)
    print("Horas para usar restantes:", calcular_horas_libres(duracion_tiempo_libre))
#Pide un tiempo libre hasta que las horas sean validas y muestra los resultados obtenidos


def main():
    otro_dia = "Si"
    while otro_dia == "Si":
        Actividad_a_programar = leer_opcion("Ingresa tu tipo de hora, Ocupada o Libre: ", "Ocupada", "Libre")
        if Actividad_a_programar == "Ocupada":
            programar_ocupada()
        else:
            programar_libre()
        otro_dia = leer_opcion("Programar otro dia? Si o No: ", "Si", "No")

if __name__ == "__main__":
    main()