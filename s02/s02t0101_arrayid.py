import array as arr


#Crear un arreglo
# i: Entero con signo
# I: Entero sin signo
# f: Numeros decimales
# d: Numeros decimales doble
# u: Caracter unicode
my_array = arr.array('i' ,[10,22,300,1,12,63,43])

#Interaccion automatica
#for num in my_array:
    #print(num)

#Acceso individual a los elementos
#print(my_array[0])
#print(my_array[1])
#print(my_array[1])

print(len(my_array))

#for i in range(len(my_array)):
    #if my_array[i]%2==0:
       # print(f"Elemento {i+1}: {my_array[i]}")

#Busqueda de un elemento
num_to_serch = 45 

try: 
    print(f"Localizando 1:{my_array.index (num_to_serch)}")
except:
    print("⚠️ Numero no encontrado!!")