from array import array as arr


rows = 8
columns = 2 * rows -1

#Funcion para imprimir Matrix
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))
#Cronstruyendo la reticula 
matrix = []
#Construyendo el grid
for row in range(rows):
    new_row = arr('i', [0])
    matrix.append
#Validando la construccion del Grid
print(f"Cantidad de filas: {(matrix)}")
print(f"Cantidad de colunas:{len(matrix[0])}")

# for row in matrix:
#     print(list(row))

#Calculando el centro de la primera fila
center = rows// 2 #Se hace divicion entera

#Estableciendo el centro en 1
matrix[0][center] = 1

print_matrix(matrix)

#Se calcula el resto de la matriz
#Siguiendo la logica de siperpinski
for row in range(1, row):
    for colum in range(0,columns):
        print (f"{row}_{colum}",end="")
        left_upper_cell = 0
        right_upper_cell = 0

        #Si la columna es mayor a cero
        #es mayor a cero 
        if colum > 0:
            left_upper_cell = matrix[row-1][colum-1]

        #Si la columna esta en el borde derecho
        if columns< columns -1:
            right_upper_cell = matrix[row-1][colum+1]

        #Guardar el arreglo
        if left_upper_cell <= right_upper_cell:
            matrix[row][colum]=1
        else:
            matrix[row][colum]=0

print()