HORAS_POR_DIA = 24
HORAS_POR_MOMENTO = 6
MOMENTOS = ["Amanecer", "Dia", "Tarde", "Noche"]
DIAS_DE_LA_SEMANA = ["LUNES", "MARTES", "MIERCOLES",
                     "JUEVES", "VIERNES",
                     "SABADO", "DOMINGO"]
DIGITOS_VALIDOS = "0123456789"
SEPARADOR_MENU = "-" * 40
NOMBRE_ARCHIVO_CREADO = "horario.txt"
SEPARADOR_ARCHIVO = "/"


def calcular_duracion(hora_1, hora_2):
    """Regresa la duracion entre dos horas"""
    return hora_2 - hora_1


def calcular_porcentaje_dia(duracion_correcta):
    """Regresa el porcentaje del dia que ocupa una actividad"""
    return int(duracion_correcta / HORAS_POR_DIA * 100 + 0.5)


def generar_resumen(dia, duracion, porcentaje):
    """Regresa una lista con el dia, la duracion
    y el porcentaje programados"""
    return [dia, duracion, porcentaje]


def convertir_hora(hora):
    """Convierte una hora de 0 a 24 al formato
    de horas y minutos y AM/PM"""
    minutos_totales = int(hora * 60)
    horas = minutos_totales // 60
    minutos = minutos_totales % 60
    momento = "AM"
    if horas >= 12 and horas < 24:
        momento = "PM"
    hora_12 = ((horas - 1) % 12) + 1
    texto_minutos = str(minutos)
    if minutos < 10:
        texto_minutos = "0" + texto_minutos
    return str(hora_12) + ":" + texto_minutos + " " + momento


def formato_hora(hora_1, hora_2):
    """Regresa la duracion entre dos horas en formato AM/PM"""
    return convertir_hora(hora_1) + " a " + convertir_hora(hora_2)


def horas_validas(hora_1, hora_2):
    """Indica si la hora final es mayor que la inicial,
    esto para ver si es valida o no"""
    return hora_2 > hora_1


def verificar_empalme(hora_1, hora_2, actividades):
    """Indica si el bloque nuevo se empalma con alguna actividad"""
    for actividad in actividades:
        if hora_1 < actividad[1] and actividad[0] < hora_2:
            return True
    return False


def calcular_horas_libres(horas_usadas):
    """Regresa las horas que quedan libres para el dia"""
    return HORAS_POR_DIA - horas_usadas


def momento_dia(hora_usada):
    """Regresa el momento del dia en que inicia una acividad"""
    parte_dia = int(hora_usada // HORAS_POR_MOMENTO) % 4
    return MOMENTOS[parte_dia]


def momento_dia_final(hora_final):
    """Regresa el momento del dia en el que termina una actividad"""
    return momento_dia(hora_final - 0.01)


def es_digitos(texto):
    """Indica si el texto tiene digitos y si los tiene,
    que sean digitos del 0 al 9 (osea validos)"""
    if len(texto) == 0:
        return False
    for caracter in texto:
        if caracter not in DIGITOS_VALIDOS:
            return False
    return True


def es_numero(texto):
    """Indica si el texto es un numero positivo con punto opcional"""
    if len(texto) > 10:
        return False
    partes = texto.split(".")
    if len(partes) == 1:
        return es_digitos(partes[0])
    if len(partes) == 2:
        return es_digitos(partes[0]) and es_digitos(partes[1])
    return False


def leer_opcion(mensaje, opcion_1, opcion_2):
    """Pide una opcion hasta que sea una de las dos permitidas"""
    opcion = input(mensaje).strip().lower()
    while opcion != opcion_1.lower() and opcion != opcion_2.lower():
        opcion = input("Ingresa una opcion valida: ")
        opcion = opcion.strip().lower()
    return opcion


def leer_entero(mensaje, minimo, maximo):
    """Pide un entero entre un minimo y un maximo
    hasta que cumpla el requisito"""
    numero = minimo - 1
    while numero < minimo:
        texto = input(mensaje).strip()
        if es_digitos(texto) and len(texto) <= 3:
            if minimo <= int(texto) <= maximo:
                numero = int(texto)
        if numero < minimo:
            print("Ingresa un numero entre", minimo, "y", maximo)
    return numero


def leer_texto(mensaje):
    """Pide un texto, si no se escribe algo lo vuelve a pedir"""
    texto = input(mensaje).strip()
    while len(texto) == 0:
        texto = input("Escribe algo: ").strip()
    return texto


def leer_hora(mensaje):
    """Pide una hora entre 0 y 24 hasta que la hora sea valida"""
    hora = -1.0
    while hora < 0.0:
        texto = input(mensaje).strip().replace(",", ".")
        valida = es_numero(texto)
        if valida:
            valor = float(texto)
            valida = valor <= HORAS_POR_DIA and valor * 4 == int(valor * 4)
        if valida:
            hora = valor
        else:
            print("Ingresa un numero entre 0 y 24")
    return hora


def leer_bloque(actividades, total_ocupado):
    """Pide inicio y final hasta formar un bloque valido"""
    valido = False
    while not valido:
        hora_inicio = leer_hora("Inicio actividad (0 a 24): ")
        hora_final = leer_hora("Final actividad (0 a 24): ")
        duracion = calcular_duracion(hora_inicio, hora_final)
        if not horas_validas(hora_inicio, hora_final):
            print("La hora final debe ser mayor a la inicial")
        elif verificar_empalme(hora_inicio, hora_final, actividades):
            print("Ese horario se empalma con otra actividad")
        elif total_ocupado + duracion > HORAS_POR_DIA:
            print("La actividad no puede pasar de 24 hrs en total")
        else:
            valido = True
    return hora_inicio, hora_final


def mostrar_bloque(nombre_actividad, dia, hora_inicio, hora_final,
                   duracion, porcentaje):
    """Imprime los resultados de un bloque de tiempo"""
    resumen = generar_resumen(dia, duracion, porcentaje)
    print(SEPARADOR_MENU)
    print("Tu actividad", nombre_actividad.upper(), "abarca:",
          formato_hora(hora_inicio, hora_final))
    print("Duracion:", duracion, "hrs")
    print("Porcentaje del dia usado:", porcentaje, "%")
    print("Resumen (Dia/Duracion/Uso):", resumen[0], "|",
          resumen[1], "hrs |", resumen[2], "%")
    print("Horario valido?: Si")
    print("Momento del dia en que inicia:", momento_dia(hora_inicio))
    print("Momento del dia en que termina:",
          momento_dia_final(hora_final))


def mostrar_lista_actividades(nombres, actividades):
    """Muestra las actividades registradas hasta el momento"""
    for i in range(len(actividades)):
        print("Actividad numero", i + 1, ":", nombres[i], "|",
              formato_hora(actividades[i][0], actividades[i][1]),
              "| duracion:", actividades[i][2], "hrs")


def horas_en_rango(actividades, rango_inicio, rango_fin):
    """Suma las horas de las actividades que caen dentro de un rango"""
    total = 0.0
    for actividad in actividades:
        inicio = max(actividad[0], rango_inicio)
        fin = min(actividad[1], rango_fin)
        if fin > inicio:
            total = total + fin - inicio
    return total


def horas_por_momento(actividades):
    """Regresa las horas ocupadas en cada momento del dia"""
    amanecer = horas_en_rango(actividades, 0, 6)
    dia = horas_en_rango(actividades, 6, 12)
    tarde = horas_en_rango(actividades, 12, 18)
    noche = horas_en_rango(actividades, 18, 24)
    return [amanecer, dia, tarde, noche]


def mostrar_resumen_dia(dia, nombres, actividades):
    """Muestra el resumen final de un dia programado"""
    totales = horas_por_momento(actividades)
    print(SEPARADOR_MENU)
    print("Resumen final del dia:", dia)
    for i in range(len(nombres)):
        print(i + 1, "actividad", nombres[i], "que dura:",
              actividades[i][2], "hrs")
    for i in range(len(MOMENTOS)):
        print(MOMENTOS[i], ":", totales[i], "hrs")


def programar_ocupada(dia):
    """Agrega actividades a un dia hasta terminar o llegar a 24 hrs"""
    total_ocupado = 0.0
    seguir = "si"
    actividades = []
    nombres = []
    while total_ocupado < HORAS_POR_DIA and seguir == "si":
        nombre_actividad = leer_texto("Nombre de la actividad: ")
        hora_inicio, hora_final = leer_bloque(actividades, total_ocupado)
        duracion = calcular_duracion(hora_inicio, hora_final)
        actividades.append([hora_inicio, hora_final, duracion])
        nombres.append(nombre_actividad)
        total_ocupado = total_ocupado + duracion
        porcentaje = calcular_porcentaje_dia(total_ocupado)
        mostrar_bloque(nombre_actividad, dia, hora_inicio, hora_final,
                       duracion, porcentaje)
        mostrar_lista_actividades(nombres, actividades)
        print("Horas libres restantes:",
              calcular_horas_libres(total_ocupado))
        if total_ocupado < HORAS_POR_DIA:
            seguir = leer_opcion("Agregar otra actividad? Si o No: ",
                                 "Si", "No")
    return [dia, nombres, actividades]


def programar_libre(dia):
    """Registra un bloque de tiempo libre para un dia"""
    hora_inicio, hora_final = leer_bloque([], 0.0)
    duracion = calcular_duracion(hora_inicio, hora_final)
    porcentaje = calcular_porcentaje_dia(duracion)
    mostrar_bloque("descanso", dia, hora_inicio, hora_final, duracion,
                   porcentaje)
    print("Horas para usar restantes:", calcular_horas_libres(duracion))
    return [dia, ["descanso"], [[hora_inicio, hora_final, duracion]]]


def llenar_matriz_horas(dias_programados):
    """Crea una matriz, cada fila es un dia  y cada columna un momento"""
    matriz = []
    for dia_programado in dias_programados:
        matriz.append(horas_por_momento(dia_programado[2]))
    return matriz


def mostrar_matriz_horas(dias_programados, matriz):
    """Imprime la matriz de las horas indicando el dia de cada fila"""
    print("Matriz de horas (filas = dias, columnas = momentos)")
    print("Momentos:", MOMENTOS)
    for i in range(len(matriz)):
        print(dias_programados[i][0][:3], ":", matriz[i])


def totales_por_dia(matriz):
    """Regresa las horas ocupadas en cada dia, osea la suma de cada fila"""
    totales = []
    for fila in matriz:
        totales.append(sum(fila))
    return totales


def totales_por_momento_semana(matriz):
    """Regresa las horas por momento de toda la semana"""
    totales = [0.0, 0.0, 0.0, 0.0]
    for fila in matriz:
        totales[0] = totales[0] + fila[0]
        totales[1] = totales[1] + fila[1]
        totales[2] = totales[2] + fila[2]
        totales[3] = totales[3] + fila[3]
    return totales


def actividad_mas_larga_dia(dia_programado):
    """Regresa el nombre y la duracion de la actividad mas larga"""
    nombres = dia_programado[1]
    datos = dia_programado[2]
    mayor = 0
    nombre_mayor = ""
    for i in range(len(nombres)):
        duracion = datos[i][2]
        if duracion > mayor:
            mayor = duracion
            nombre_mayor = nombres[i]
    return nombre_mayor, mayor


def actividad_mas_larga(dias_programados):
    """Regresa el dia, nombre y duracion de la actividad mas larga"""
    mayor = 0.0
    nombre_mayor = ""
    dia_mayor = ""
    for dia_programado in dias_programados:
        nombre, duracion = actividad_mas_larga_dia(dia_programado)
        if duracion > mayor:
            mayor = duracion
            nombre_mayor = nombre
            dia_mayor = dia_programado[0]
    return dia_mayor, nombre_mayor, mayor


def nombres_programados(dias_programados):
    """Regresa la lista con los nombres de los dias ya programados"""
    nombres = []
    for dia_programado in dias_programados:
        nombres.append(dia_programado[0])
    return nombres


def leer_dia(dias_programados):
    """Pide un dia de la semana que aun no este programado
    con actividades o tiempo libre"""
    programados = nombres_programados(dias_programados)
    print("Dias de la semana:")
    for i in range(len(DIAS_DE_LA_SEMANA)):
        marca = ""
        if DIAS_DE_LA_SEMANA[i] in programados:
            marca = "(ya programado)"
        print(i + 1, "-", DIAS_DE_LA_SEMANA[i], marca)
    dia = ""
    elegido = -1
    while dia == "" and elegido != 0:
        elegido = leer_entero("Dia a programar (0 para cancelar): ", 0, 7)
        if elegido != 0:
            if DIAS_DE_LA_SEMANA[elegido - 1] in programados:
                print("Ese dia ya esta programado")
            else:
                dia = DIAS_DE_LA_SEMANA[elegido - 1]
    return dia


def agregar_dia(dias_programados, es_ocupado):
    """Programa un dia nuevo, ya sea con actividades o libre"""
    if len(dias_programados) == len(DIAS_DE_LA_SEMANA):
        print("Ya programaste los 7 dias,elimina uno para poder cambiarlo")
    else:
        dia = leer_dia(dias_programados)
        if dia == "":
            print("Programacion cancelada")
        elif es_ocupado:
            dias_programados.append(programar_ocupada(dia))
        else:
            dias_programados.append(programar_libre(dia))


def ver_resumenes(dias_programados):
    """Muestra el resumen de todos los dias programados por el usuario"""
    if len(dias_programados) == 0:
        print("Aun no hay dias programados")
    for dia_programado in dias_programados:
        mostrar_resumen_dia(dia_programado[0], dia_programado[1],
                            dia_programado[2])


def ver_estadisticas(dias_programados):
    """Muestra la matriz de horas y las estadisticas de
    la semana programada"""
    if len(dias_programados) == 0:
        print("Aun no hay dias programados")
    else:
        matriz_horas = llenar_matriz_horas(dias_programados)
        print(SEPARADOR_MENU)
        mostrar_matriz_horas(dias_programados, matriz_horas)
        print("Horas ocupadas por dia:", totales_por_dia(matriz_horas))
        print("Horas ocupadas por momento (todos los dias):",
              totales_por_momento_semana(matriz_horas))
        print("Actividad mas larga (Dia/Nombre/Duracion):",
              actividad_mas_larga(dias_programados))


def eliminar_dia(dias_programados):
    """Elimina un dia programado despues de que el usuario lo confirme"""
    if len(dias_programados) == 0:
        print("Aun no hay dias programados")
    else:
        for i in range(len(dias_programados)):
            print(i + 1, "-", dias_programados[i][0])
        dia_elegido = leer_entero("Dia a eliminar (0 para cancelar): ", 0,
                                  len(dias_programados))
        if dia_elegido != 0:
            confirmar = leer_opcion("Seguro? Si o No: ", "Si", "No")
            if confirmar == "si":
                dias_programados.pop(dia_elegido - 1)
                print("Dia eliminado")


def guardar_horario(dias_programados):
    """Guarda los dias programados en el archivo, una actividad por linea"""
    if len(dias_programados) == 0:
        print("Aun no hay dias programados para guardar")
    else:
        archivo = open(NOMBRE_ARCHIVO_CREADO, "w")
        for dia_programado in dias_programados:
            for i in range(len(dia_programado[1])):
                nombre = dia_programado[1][i].replace(SEPARADOR_ARCHIVO, "/")
                actividad = dia_programado[2][i]
                archivo.write(dia_programado[0] + SEPARADOR_ARCHIVO +
                              nombre + SEPARADOR_ARCHIVO +
                              str(actividad[0]) + SEPARADOR_ARCHIVO +
                              str(actividad[1]) + "\n")
        archivo.close()
        print("Horario guardado en", NOMBRE_ARCHIVO_CREADO)


def mostrar_menu():
    """Imprime las opciones a modo de menu"""
    print(SEPARADOR_MENU)
    print("MENU PRINCIPAL")
    print("1- Programar un dia con actividades")
    print("2- Programar un dia libre")
    print("3- Ver resumen de los dias")
    print("4- Ver matriz y estadisticas de la semana")
    print("5- Eliminar un dia programado")
    print("6- Guardar horario en archivo")
    print("7- Salir")


dias_programados = []
opcion = 0
while opcion != 7:
    mostrar_menu()
    opcion = leer_entero("Elige una opcion (1 a 7): ", 1, 7)
    if opcion == 1:
        agregar_dia(dias_programados, True)
    elif opcion == 2:
        agregar_dia(dias_programados, False)
    elif opcion == 3:
        ver_resumenes(dias_programados)
    elif opcion == 4:
        ver_estadisticas(dias_programados)
    elif opcion == 5:
        eliminar_dia(dias_programados)
    elif opcion == 6:
        guardar_horario(dias_programados)
print("Bye")
