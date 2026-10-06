""""
NOTAS
1. Identifico el tamaño de la entrada "n"
El tamaño de la entada es el numero
de estudiantes
2. Es ver cuanto crecel el numero de 
operaciones en el algoritmo conforme
crece el tamaño de la entrada
Agrego las BigO encontradas 
O(n) + O(4) = 0(n+4) = 
"""
#Creando una lists de etudiantes
student_list_01 = ['Max', 'Esteban', 'Colapinto', 'George']
student_list_02 = ['Isack', 'Oliver', 'Gasly', 'Kimi']

# Verificando presencia de un estudiante
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student:
            print("✅Estudiante Encontado")#O(1)
            return student
    #Si no encuentro al estudiante
    print("❌Estudiante no encontrado")#O(1)
    return None#O(1)

#Probando Algoritmo
check_student("Gasly", student_list_02)#O(1)