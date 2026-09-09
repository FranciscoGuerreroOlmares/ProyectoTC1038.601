horaact = float(input("Escribe tu hora actual:"))
dia1 = input("Escribe el dia que quieres programar:")
hora1 = float(input("Inicio actividad:"))
hora2 = float(input("Final actividad:"))
'''Variables ingresadas por el usuario que usara el codigo, son del tipo str y float ya que 
se pueden definir las horas con minutos usando un punto (.) en lugar de dos puntos (:) '''

def dur(a, b):
    return b-a
duracion = dur(hora1, hora2)
#Funcion utilizada pra definir la duracion total de la actividad por medio de una resta (hora2 menos hora1)

def percent(a):
    return (a / 24) * 100
porcentaje = percent(duracion)
#Funcion utilizada para ver que porcentaje del dia ha sido utilizado hasta el momento (duracion dividido por 24 y multiplicado por 100)

def resum(a, b, c):
    return a, b, c
resumen = resum(dia1, duracion, porcentaje)
#Funcion utilizada para mostrarle al usuario el plan para el dia
   
print("Duracion de la actividad:", duracion, "hrs/hr")
print("Porcentaje del dia usado:", porcentaje, "%")
print("Resumen de tu dia (Dia/Duracion/Uso):", resumen)
#Imprime resultados de las funciones de acuerdo a los valores asignados por el usuario

hora3 = float(input("Inicio de tiempo libre:"))
hora4 = float(input("Final de tiempo libre:"))
#Ingreso de nuevas horas por el usuario para definir sus horas libres

duracion2 = dur(hora3, hora4)
#Usando la funcion dur, realiza una resta de hora 4 menos hora3
print("Duracion de tu tiempo libre", duracion2, "hrs/hr")
#Imprime resultado de la resta

porcentaje2 = percent(duracion2) + porcentaje
#Reutilizando la funcion percent

print("Porcentaje de tu dia usado en total:", porcentaje2, "%")
#Imprimir nuevo porcentaje

resumen2 = resum(dia1, duracion2, porcentaje2)
#Reutilizacion de la funcion resum
print("Resumen de tu descanso (Dia/Duracion/Uso)", resumen2)
#Imprimir nuevo resumen
