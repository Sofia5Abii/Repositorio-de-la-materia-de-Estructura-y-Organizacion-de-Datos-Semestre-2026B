from array import array as arr

# Paramestros de mi cuadricula
rows = 15
columns = 2 * rows - 1

# Funcion para imprimir matrix
def print_matrix(input_matrix):
  for row in input_matrix:
    print(list(row))

# Creando el grid 2D
matrix = []
# Construyendo el grid
for _ in range(rows):
  new_row = arr('i', [0] * columns)
  matrix.append(new_row)

# Validando la construccion del Grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

# Calculando el centro de la primera fila
center = columns // 2 # se hace divisione entera

# Estableciendo el centro en 1
matrix[0][center] = 1

# print_matrix(matrix)

# Se calcula el resto de la matrix
# Siguiendo la logica del siperpinsky Gasket
for row in range(1,rows):
  for col in range(0,columns):
    left_upper_cell = 0
    right_upper_cell = 0

    # Si la columna donde estamos
    # es mayor a cero es decir esta un elemento

    # despues del borde izquierdo
    if col > 0:
      left_upper_cell = matrix[row-1][col-1]

    # Si la columna esta un elmento antes
    # del borde derecho
    if col < columns - 1:
      right_upper_cell = matrix[row-1][col+1]

    # Guardo el arrelgo
    if left_upper_cell != right_upper_cell :
      matrix[row][col] = 1
    else:
      matrix[row][col] = 0

print()
print_matrix(matrix)

# Continuamos aqui
def draw_matrix(input_matrix, symbol="*"):
  for row in input_matrix:
    for cell in row:
      if cell == 1:
        print(CYAN + symbol + RESET, end="")
      else:
        print(RED + " " + RESET, end="")
    print()

# ANSI color codes
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

draw_matrix(matrix)

from array import array as arr

# Borra pantalla con caracteres ANSI
def clear_screen():
  print("\033[2J\033[H", end="")

from array import array as arr
from enum import Enum

# Borra pantalla con caracteres ANSI
def clear_screen():
  print("\033[2J\033[H", end="")

# Encapsulado de los valores ANSI
# para colores en un enumerado
class AnsiColor(Enum):
  RED = "\033[91m"
  YELLOW = "\033[93m"
  CYAN = "\033[96m"
  RESET = "\033[0m"

# Funcion para imprimir matrix
def print_matrix(input_matrix):
  for row in input_matrix:
    print(list(row))

# Funcion para generar triangulo
def generate_triangle(rows = 1):
  # Paramestros de mi cuadricula
  columns = 2 * rows - 1
  # Creando el grid 2D
  matrix = []
  # Construyendo el grid
  for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)
  # Calculando el centro de la primera fila
  center = columns // 2 # se hace divisione entera

  # Estableciendo el centro en 1
  matrix[0][center] = 1

  # Se calcula el resto de la matrix
  # Siguiendo la logica del siperpinsky Gasket
  for row in range(1,rows):
    for col in range(0,columns):
      left_upper_cell = 0
      right_upper_cell = 0

      # Si la columna donde estamos
      # es mayor a cero es decir esta un elemento
      # despues del borde izquierdo
      if col > 0:
        left_upper_cell = matrix[row-1][col-1]

      # Si la columna esta un elmento antes
      # del borde derecho
      if col < columns - 1:
        right_upper_cell = matrix[row-1][col+1]

      # Asigno valor al arreglo
      if left_upper_cell != right_upper_cell :
        matrix[row][col] = 1
      else:
        matrix[row][col] = 0
  # Regresando la matriz
  return matrix

# Dibuja la matriz
def draw_matrix(input_matrix, symbol="*"):
  for row in input_matrix:
    for cell in row:
      if cell == 1:
        print(AnsiColor.CYAN.value + symbol + AnsiColor.RESET.value, end="")
      else:
        print(AnsiColor.RED.value + " ", end="")
    print()
# Metodo principal
def main():
  # Genera el triangulo de Sierpinsky
  matrix = generate_triangle(5)
  # Limpia la pantalla antes de dibujar la matriz
  clear_screen()
  # Dibuja la matriz en pantalla
  draw_matrix(matrix, symbol="■")

if __name__ == "__main__":
  main()
