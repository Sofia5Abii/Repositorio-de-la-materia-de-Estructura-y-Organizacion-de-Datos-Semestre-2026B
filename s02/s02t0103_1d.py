from array import array as arr

from s02t0102_Array import print_array 

my_array = arr('i',[2,10,15,20])

print("--- ANTES DE LA INSECION ---")
print_array(my_array)

#incerción
my_array.insert(1,98)
print("--- DESPUES DE LA INSECION ---")
print_array(my_array)