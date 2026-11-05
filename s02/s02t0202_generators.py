"""
Generadores

Los generadores son funciones que pueden
pausar su ejecucion

Cuando se invoca una funcion generadora
devuelve un objeto generado(aka, Iterador)

El codigo dentro de la funcion no  se ejecuta
de inmediato, solo se compila

La funcion se ejecuta unicamente cuando
iteras sobre el generador.
"""

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
print(my_generator())

#Se invoca funcion generadora
my_interator=my_generator

#Se itera manualmente sobre el generador
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))

#Los iteradores se pueden iterar con un for
for value in my_interator:
    print(value)