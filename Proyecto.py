def calcular_duracion(hora_1, hora_2):
    return hora_2 - hora_1
#Ejecuta una resta para determinar el tiempo total transcurrido


def calcular_porcentaje_dia(duracion_correcta):
    return duracion_correcta / 24 * 100
#Realiza una division seguida de una multiplicacion para calcular el porcentaje del dia usado


def generar_resumen(dia, duracion, porcentaje):
    return dia, duracion, porcentaje
#Genera un resumen en base a los datos obtenidos previamente


def formato_hora(hora_1, hora_2):     
    hora_programada_i = ((hora_1 - 1) % 12) + 1
    hora_programada_f = ((hora_2 - 1) % 12) + 1
    momento_del_dia = input("Ingresa el momento del dia, AM o PM: ")
    return hora_programada_i, momento_del_dia, "a", hora_programada_f, momento_del_dia
#Acomoda las horas ingresadas al formato de AM/PM por medio de una resta, seguido de su residuo al dividirse entre 12


def horas_validas(hora_1, hora_2):
    if hora_2 > hora_1:
        return "Horas validas"
    else:
        return "Ingrese horas validas"
#Compara horas ingresadas para determinar si son posibles o irreales


def calcular_horas_libres(calcular_duracion):
    return 24 - calcular_duracion
#Ejecuta una resta para determinar las horas libres restantes


def momento_dia(hora_usada):
    parte_dia = int(hora_usada // 4) % 4
    if parte_dia == 0:
        return "Break of day"
    elif parte_dia == 1:
        return "Morning"
    elif parte_dia == 2:
        return "Afternoon"
    else:
        return "Night"
#Por medio de una division entera de la hora entre 4 y posterior reciproco de ese resultado entre 4 para determinar en que momento del dia inicia la actividad


def main ():
    Actividad_a_programar = input("Ingresa tu tipo de hora, Ocupada o Libre.: ")
    if Actividad_a_programar == "Ocupada" :
        dia = input("Escribe el dia que quieres programar: ")
        hora_inicio_actividad = float(input("Inicio actividad: "))
        hora_final_actividad = float(input("Final actividad: "))
#Ingreso de parametros del usuario
          
        inicio_fin_actividad = formato_hora(hora_inicio_actividad, hora_final_actividad)
        duracion_actividad = calcular_duracion(hora_inicio_actividad, hora_final_actividad)
        porcentaje_dia = calcular_porcentaje_dia(duracion_actividad)
        resumen_actividad = generar_resumen(dia, duracion_actividad, porcentaje_dia)   
        validacion_horas = horas_validas(hora_inicio_actividad, hora_final_actividad) 
        horas_libres = calcular_horas_libres(duracion_actividad) 
        momento_inicio_actividad = momento_dia(hora_inicio_actividad)
        momento_fin_actividad = momento_dia(hora_final_actividad)
#Creacion de variables para ejecutar las funciones con los parametros ingresados para una actividad
  
        if duracion_actividad < 24:
            print("Tu actividad abarca:", inicio_fin_actividad)
            print("Duracion de la actividad:", duracion_actividad, "hrs/hr")
            print("Porcentaje del dia usado:", porcentaje_dia, "%")
            print("Resumen de tu dia (Dia/Duracion/Uso):", resumen_actividad)
            print("Horario valido?:", validacion_horas)
            print("Horas libres restantes:", horas_libres)
            print("Momento del dia en que inicia la actividad:", momento_inicio_actividad)
            print("Momento del dia en que termina la actividad:", momento_fin_actividad)

        else: 
            print("Ingrese horas validas")
#Imprimir resultados obtenidosn solo si la duracion de la actividad es real(menor a 24 hrs), si no notificar al usuario que no es valido
        
        
    elif Actividad_a_programar == "Libre":
        dia_libre = input("Escribe el dia que quieres programar: ")
        hora_inicio_tiempo_libre = float(input("Inicio de tiempo libre: "))
        hora_final_tiempo_libre = float(input("Final de tiempo libre: "))  
#Ingreso de parametros del usuario

        inicio_fin_actividad = formato_hora(hora_inicio_tiempo_libre, hora_final_tiempo_libre)
        duracion_tiempo_libre = calcular_duracion(hora_inicio_tiempo_libre, hora_final_tiempo_libre)      
        porcentaje_dia_libre = calcular_porcentaje_dia(duracion_tiempo_libre) 
        resumen_tiempo_libre = generar_resumen(dia_libre, duracion_tiempo_libre, porcentaje_dia_libre) 
        validacion_horas_libres = horas_validas(hora_inicio_tiempo_libre, hora_final_tiempo_libre) 
        horas_disponibles = calcular_horas_libres(duracion_tiempo_libre) 
        momento_inicio_libre = momento_dia(hora_inicio_tiempo_libre)
        momento_fin_libre = momento_dia(hora_final_tiempo_libre)
#Creacion de variables para ejecutar las funciones con los parametros ingresados para un tiempo libre
          
        print("Tu descanso abarca:", inicio_fin_actividad)
        print("Duracion de tu tiempo libre", duracion_tiempo_libre, "hrs/hr")
        print("Porcentaje de tu dia usado:", porcentaje_dia_libre, "%")
        print("Resumen de tu descanso (Dia/Duracion/Uso)", resumen_tiempo_libre)
        print("Horario valido?:", validacion_horas_libres)
        print("Horas para usar restantes:", horas_disponibles)
        print("Momento del dia en que inicia el tiempo libre:", momento_inicio_libre)
        print("Momento del dia en que termina el tiempo libre:", momento_fin_libre)

    else:
        print("Escribe una opcion valida")
#Imprimir resultados obtenidosn solo si la duracion de la actividad es real(menor a 24 hrs), si no notificar al usuario que no es valido

if __name__ == "__main__": 
    main()
 














