from nodo import nodo

class ColaPrioridad:
    def __init__(self):
        self.__list = None

    def enqueue(self, persona):
        nuevo_nodo = nodo(persona)
        if persona.getEdad() >= 65:
            if self.__list is None or self.__list.getData().getEdad() < 65:
                nuevo_nodo.setNext(self.__list)
                self.__list = nuevo_nodo
            else:
                current = self.__list
                while current.getNext() is not None and current.getNext().getData().getEdad() >= 65:
                    current = current.getNext()
                nuevo_nodo.setNext(current.getNext())
                current.setNext(nuevo_nodo)
        else:
            if self.__list is None:
                self.__list = nuevo_nodo
            else:
                current = self.__list
                while current.getNext() is not None:
                    current = current.getNext()
                current.setNext(nuevo_nodo)

    def dequeue(self):
        if self.__list is None:
            print("La cola está vacía, por lo tanto, no hay nada que sacar...")
            return None
        persona_atendida = self.__list.getData()
        self.__list = self.__list.getNext()
        print(f"Persona atendida: {persona_atendida}")
        return persona_atendida

    def imprimir(self):
        current = self.__list
        count = 0
        while current is not None:
            print(current.getData())
            current = current.getNext()
            count += 1
        print(f"Total de personas en la lista: {count}")