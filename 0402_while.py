"""
Escribir un programa que calcule la suma de los "n" números naturales.
Por Ejemplo sin 100, el programa calculara la suma del 1 al 100
"""
#importamos biblioteca time
import time

# Función que suma los primeros n números naturales usando while
def sum_of_n(n):
    total_sum = 0
    number = 1

    while number <= n:
        total_sum = total_sum + number
        number += 1

    return total_sum


dataset = []

repetition = 1
while repetition <= 10:
    # Tomando el tiempo inicial
    timestamp_01 = time.time()

    # Sumar los n números
    n = repetition * 500
    result = sum_of_n(n)

    # Tomando el tiempo final
    timestamp_02 = time.time()

    elaps_time = round((timestamp_02 - timestamp_01) * 1e6,ndigits=2)

    # Agregar datos al dataset
    dataset.append((n, elaps_time, result))

    repetition += 1

# Imprimir dataset
for tup in dataset:
    print(tup)