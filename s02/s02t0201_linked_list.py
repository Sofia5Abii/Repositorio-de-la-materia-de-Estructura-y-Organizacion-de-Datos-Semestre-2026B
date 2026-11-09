#Creando loa clase Nodo
class Node:
    #Constructor
    def __init__(self, data=None):
        self.data = data 
        self.next = None
    def iter(self):
        current = self
        while current:
            value = current.data
            current = current.next
            yield value

#Creando una funcion principal
def main():
    #Testear la clase Nodo
    node_01 = Node("eggs")
    node_02 = Node("ham")
    node_03 = Node("bacon")

    #print("🔗NODES SIN ENLASAR🔗")
    #print(f"Node 01: D:{node_01.data} - N:{node_01.next}")
    #print(f"Node 02: D:{node_02.data} - N:{node_02.next}")
    #print(f"Node 03: D:{node_03.data} - N:{node_03.next}")

    #Enlasando nodos
    node_01.next = node_02
    node_02.next = node_03

    #print("🔗NODES ENLASADOS🔗")
    #print(f"Node 01: D:{node_01.data} - N:{node_01.next}")
    #print(f"Node 02: D:{node_02.data} - N:{node_02.next}")
    #print(f"Node 03: D:{node_03.data} - N:{node_03.next}")

    # List Traversal (Recorrido de la lista)
    for node_value in node_01.iter():
        print(node_value)

#Invocando a Main
if __name__ == "__main__":
    main()