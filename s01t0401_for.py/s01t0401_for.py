"""
Escribir un programa que calcule la suma de los "n" números naturales.
Por Ejemplo sin 100, el programa calculara la suma del 1 al 100
"""
#importamos biblioteca time
import time

#funcion que suma los primeros n numeros naturales
def sum_of_n(n):
    total_sum = 0
    #Sumando lo n numeros
    #Ciclo for
    for number in range(1, n+1):
     total_sum = total_sum + number
    return total_sum

dataset = []

for repettion in range(1,11):
   #tomar el tiempo
    #Tomando el tiempo final
    timestamp_01 = time.time()
    #Sumar los n numeros
    n = repettion * 500 
    result = sum_of_n(n)

    #⌛Tomando el tiempo final
    timestamp_02 = time.time()

    elaps_time = round((timestamp_02 - timestamp_01 ) * 1e6,2)

    #Agregar la tripleta de los datos al data set
    dataset.append((n,elaps_time,result) )

    #imprimir el dataset
    #dataset = [] #(n,time_sum)


   
for tup in dataset:
    print(tup)