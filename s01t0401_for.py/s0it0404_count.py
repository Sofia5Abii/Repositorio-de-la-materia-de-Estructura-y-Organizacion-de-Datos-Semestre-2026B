# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(1)
student_list_01 = ['Jordan','Pipen','Curry','Shack', 'Monroy', 'Arlette,', 'Palestina']
def random_function(students):
    first = students[0] # O(1)
    total = 0 # O(1)
    new_list = [] # O(1)

    for student in students:
        total += 1 # O(1)
        new_list.append(student) # O(n)

    print(new_list)
    print ("Se le suma 1 al total")
    total += 1
    new_list.append(student)
    print("Imprimiendo estudiantes")
    print(new_list) # O(n)/O(1)
    return total # O(1)

print(f"Tamaño de la lista: {len(student_list_01)}")
print(random_function(student_list_01))
print("")

# Calcular O(2n)+O(5)=O(2n+5) = O(n)