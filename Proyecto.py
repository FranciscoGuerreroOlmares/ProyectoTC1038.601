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
    momentos = ["Break of day", "Morning", "Afternoon", "Night"]
    parte_dia = int(hora_usada // 6) % 4
    return momentos[parte_dia]
#Por medio de una division entera de la hora entre 6 y su residuo entre 4 para determinar en que momento del dia cae la hora, determinandolo por su posicion en una lista
 
 
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
 
 
def mostrar_bloque(nombre_actividad, dia, hora_inicio, hora_final, duracion, porcentaje):
    print("Tu actividad", nombre_actividad, "abarca:", formato_hora(hora_inicio, hora_final))
    print("Duracion:", duracion, "hrs/hr")
    print("Porcentaje del dia usado:", porcentaje, "%")
    print("Resumen (Dia/Duracion/Uso):", generar_resumen(dia, duracion, porcentaje))
    print("Horario valido?:", horas_validas(hora_inicio, hora_final))
    print("Momento del dia en que inicia:", momento_dia(hora_inicio))
    print("Momento del dia en que termina:", momento_dia(hora_final))
#Imprime los resultados de un bloque de tiempo en base a lo registrado por el usuario
 
 
def mostrar_lista_actividades(actividades):
    i = 1
    for actividad in actividades:
        print("Actividad numero", i, ":", formato_hora(actividad[0], actividad[1]), "con duracion:", actividad[2])
        i = i + 1
#Muestra al terinar de definir un dia un resumen de este con ayuda de un ciclo for
 
 
def horas_por_momento(actividades):
    totales = [0, 0, 0, 0]
    for actividad in actividades:
        parte_dia = int(actividad[0] // 6) % 4
        totales[parte_dia] = totales[parte_dia] + actividad[2]
    return totales
#Funcion que muestra el total de horas ocupadas en cada momento del dia (morning, break of the day, etc), con ayuda de listas y un ciclo for

 
def mostrar_resumen_dia(dia, nombres, actividades):
    momentos = ["Break of day", "Morning", "Afternoon", "Night"]
    totales = horas_por_momento(actividades)
    print("Resumen final del dia:", dia)
    for i in range(len(nombres)):
        print(i + 1,"actividad", nombres[i], "que dura:", actividades[i][2], "hrs")
    for i in range(len(momentos)):
        print(momentos[i], ":", totales[i], "hrs")
#Funcion que realiza un resumen acumulativo total aclarando el dia que se esta programando con ayuda de listas y siendo entregado al usuario a finalizar su horario
 
 
def programar_ocupada():
    dia = input("Escribe el dia que quieres programar: ")
    total_ocupado = 0
    seguir = "Si"
    actividades =[]
    nombres = []
    while total_ocupado < 24 and seguir == "Si":
        nombre_actividad = input("Ingresa el nombre de tu actividad a programar: ")
        hora_inicio_actividad = leer_hora("Inicio actividad: ")
        hora_final_actividad = leer_hora("Final actividad: ")
        while horas_validas(hora_inicio_actividad, hora_final_actividad) != "Horas validas" or total_ocupado + calcular_duracion(hora_inicio_actividad, hora_final_actividad) > 24:
            print("Ingrese horas validas, la actividad no puede pasar de 24 hrs en total")
            hora_inicio_actividad = leer_hora("Inicio actividad: ")
            hora_final_actividad = leer_hora("Final actividad: ")
        duracion_actividad = calcular_duracion(hora_inicio_actividad, hora_final_actividad)
        actividades.append([hora_inicio_actividad, hora_final_actividad, duracion_actividad])
        nombres.append(nombre_actividad)
        total_ocupado = total_ocupado + duracion_actividad
        porcentaje_dia = calcular_porcentaje_dia(total_ocupado)
        mostrar_bloque(nombre_actividad, dia, hora_inicio_actividad, hora_final_actividad, duracion_actividad, porcentaje_dia)
        mostrar_lista_actividades(actividades)
        print("Horas libres restantes:", calcular_horas_libres(total_ocupado))
        if total_ocupado < 24:
            seguir = leer_opcion("Agregar otra actividad? Si o No: ", "Si", "No")
    return [dia, nombres, actividades]
#Agrega actividades del dia hasta que el usuario quiera terminar o se completen las 24 hrs
 
 
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
    return [dia_libre, ["descanso"], [[hora_inicio_tiempo_libre, hora_final_tiempo_libre, duracion_tiempo_libre]]]
#Pide un tiempo libre hasta que las horas sean validas y muestra los resultados obtenidos


def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz
#Crea una matriz con ceros para ingesar datos posteriormente


def llenar_matriz_horas(dias_programados):
    matriz = crear_matriz(len(dias_programados), 4)
    for i in range(len(dias_programados)):
        totales = horas_por_momento(dias_programados[i][2])
        for j in range(4):
            matriz[i][j] = totales[j]
    return matriz
#Llena la matriz creada anteriormente, cada fila es un dia y cada columna un momento del dia (Break of day, Morning, Afternoon, Night)


def mostrar_matriz_horas(dias_programados, matriz):
    momentos = ["Break of day", "Morning", "Afternoon", "Night"]
    print("Matriz de horas (filas = dias, columnas = momentos del dia)")
    print("Momentos:", momentos)
    for i in range(len(matriz)):
        print(dias_programados[i][0], ":", matriz[i])
#Imprime la matriz fila por fila indicando a que dia corresponde cada una


def totales_por_dia(matriz):
    totales = []
    for fila in matriz:
        suma = 0
        for valor in fila:
            suma = suma + valor
        totales.append(suma)
    return totales
#Suma cada fila de la matriz y regresa las horas ocupadas por cada dia 


def totales_por_momento_semana(matriz):
    totales = [0, 0, 0, 0]
    for fila in matriz:
        for j in range(4):
            totales[j] = totales[j] + fila[j]
    return totales
#Suma cada columna de la matriz para obtener las horas ocupadas por momentos (Break of day, Morning, Afternoon, Night) en todos los dias


def actividad_mas_larga(dias_programados):
    mayor = 0
    nombre_mayor = ""
    dia_mayor = ""
    for dia_programado in dias_programados:
        for i in range(len(dia_programado[2])):
            if dia_programado[2][i][2] > mayor:
                mayor = dia_programado[2][i][2]
                nombre_mayor = dia_programado[1][i]
                dia_mayor = dia_programado[0]
    return dia_mayor, nombre_mayor, mayor
#Recorre la lista anidada [dia, nombres, actividades] para encontrar la actividad de mayor duracion
 
 
def main():
    otro_dia = "Si"
    dias_programados = []
    while otro_dia == "Si":
        Actividad_a_programar = leer_opcion("Ingresa tu tipo de hora, Ocupada o Libre: ", "Ocupada", "Libre")
        if Actividad_a_programar == "Ocupada":
            dias_programados.append(programar_ocupada())
        else:
            dias_programados.append(programar_libre())
        otro_dia = leer_opcion("Programar otro dia? Si o No: ", "Si", "No")
    for dia_programado in dias_programados:
        mostrar_resumen_dia(dia_programado[0], dia_programado[1], dia_programado[2])
    matriz_horas = llenar_matriz_horas(dias_programados)
    mostrar_matriz_horas(dias_programados, matriz_horas)
    print("Horas ocupadas por dia:", totales_por_dia(matriz_horas))
    print("Horas ocupadas por momento (todos los dias):", totales_por_momento_semana(matriz_horas))
    print("Actividad mas larga (Dia/Nombre/Duracion):", actividad_mas_larga(dias_programados))
 
if __name__ == "__main__":
    main()