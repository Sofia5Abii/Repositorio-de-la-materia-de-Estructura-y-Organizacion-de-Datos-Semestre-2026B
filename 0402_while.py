"""
Escribir un programa que calcule la suma de los "n" números naturales.
Por Ejemplo sin 100, el programa calculara la suma del 1 al 100
"""
#importamos biblioteca time
import time
#
n = 100
the_sum = 0
#Tomamaos el t1
timestamp_01 = time.time()
#iniciando la suma
#100
while(n>0):
    the_sum=the_sum+n
    n=n-1
#Tomamos la solucion 
timestamp_02 = time.time()
#Imprimimos la solucion 
print(f"La suma es{the_sum}")
#Calculamos el tiempo
elaps_time = round((timestamp_02 - timestamp_01 ) * 1e6,ndigits=2)
print(f"Tiempo de ejecucion: {elaps_time}us")
