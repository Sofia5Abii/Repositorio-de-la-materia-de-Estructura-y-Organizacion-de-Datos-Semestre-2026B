"""
Escribir un programa que calcule la suma de los "n" números naturales.
Por Ejemplo sin 100, el programa calculara la suma del 1 al 100
"""
#importamos biblioteca time
import time

#Tomando el tiempo final
timestamp_01 = time.time()

#Programa que calcule las sumas
#de los "n" numeros naturales
n = 100
total_sum = 0

#Ciclo for
for number in range(1, n+1):
    total_sum = total_sum + number
    #1: sum <- 0 +1
    #sum = 1 
    #2: sum <- 1 + 2
    #sum = 3
    #sum <- 3 + 3
    #...
    #100: sum <- antSum + 100
    print(f"La suma de uno hasta {n} es: {total_sum}")

    #Tomando el tiempo inicial
    timestamp_02 = time.time()

    #impreción del tiempo de ejecucion
    print(f"Tiempo de ejecucion: {(timestamp_02 - timestamp_01 ) * 1e6:.2f} μs")