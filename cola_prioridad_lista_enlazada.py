from nodo import nodo

class ColaPrioridad:
    def __init__(self):
        self.__list = None

    def insercion(self, persona):
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

    def eliminar(self, posicion):
        if self.__list is None:
            print("La lista esta vacia, por lo tanto, no hay nada que borrar...")
            return
        if posicion == 0:
            self.__list = self.__list.getNext()
            return
        current = self.__list
        for i in range(posicion - 1):
            if current.getNext() is None:
                print(f"La posicion que indicaste esta fuera del rango, la lista tiene {i + 1} elementos.")
                return
            current = current.getNext()
        if current.getNext() is None:
            print(f"La posicion que indicaste esta fuera del rango {posicion} elementos.")
            return
        current.setNext(current.getNext().getNext())
        print(f"Elemento en la posición {posicion} ha sido eliminado.")

    def imprimir(self):
        current = self.__list
        while current is not None: #Recorre todos los elementos de la lista
            print(current.getData())
            current = current.getNext()

    def buscar_por_edad(self, edad):
        current = self.__list
        found = False
        while current is not None: #Recorre todos los elementos de la lista
            if current.getData().getEdad() == edad:
                print(current.getData())
                found = True
            current = current.getNext()
        if not found:
            print(f"Nadie tiene la edad {edad}")

    def buscar_por_nombre(self, nombre):
        current = self.__list
        found = False
        while current is not None:
            if nombre in current.getData().getNombre():
                print(current.getData())
                found = True
            current = current.getNext()
        if not found:
            print(f"Nadie tiene el nombre que contiene {nombre}")

    def buscar_por_apellido(self, apellido):
        current = self.__list
        found = False
        while current is not None:
            if apellido in current.getData().getApellido1() or apellido in current.getData().getApellido2():
                print(current.getData())
                found = True
            current = current.getNext()
        if not found:
            print(f"Nadie tiene el apellido que contiene {apellido}")