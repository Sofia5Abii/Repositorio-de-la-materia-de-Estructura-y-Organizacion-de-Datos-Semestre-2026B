from array import array as arr


rows = 8
columns = 2 * rows -1

#Cronstruyendo la reticula 
matrix = []
#Construyendo el grid
for row in range(rows):
    new_row = arr('i', [0])
    matrix.append

#Validando la construccion del Grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de colunas:{len(matrix[0])}")

for row in matrix:
    print(list(row))