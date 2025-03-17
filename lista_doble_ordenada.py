from nodo_doble_enlace import nodo_doble

class ListaDobleOrdenada:
    def __init__(self):
        self.__list = None

    def insercion(self, persona):
        nuevo_nodo = nodo_doble(persona)
        if self.__list is None or self.__list.getData().getEdad() >= persona.getEdad():
            nuevo_nodo.setNext(self.__list)
            if self.__list is not None:
                self.__list.setPrev(nuevo_nodo)
            self.__list = nuevo_nodo
        else:
            current = self.__list
            while current.getNext() is not None and current.getNext().getData().getEdad() < persona.getEdad():
                current = current.getNext()
            nuevo_nodo.setNext(current.getNext())
            if current.getNext() is not None:
                current.getNext().setPrev(nuevo_nodo)
            nuevo_nodo.setPrev(current)
            current.setNext(nuevo_nodo)

    def eliminar(self, posicion):
        if self.__list is None:
            print("La lista está vacía.")
            return
        if posicion == 0:
            self.__list = self.__list.getNext()
            if self.__list is not None:
                self.__list.setPrev(None)
            return
        current = self.__list
        for i in range(posicion - 1):
            if current.getNext() is None:
                print(f"Posición fuera de rango. La lista tiene {i + 1} elementos.")
                return
            current = current.getNext()
        if current.getNext() is None:
            print(f"Posición fuera de rango. La lista tiene {posicion} elementos.")
            return
        current.getNext().setPrev(current.getPrev())
        current.setNext(current.getNext().getNext())
        print(f"Elemento en la posición {posicion} ha sido eliminado.")

    def imprimir(self):
        current = self.__list
        while current is not None:
            print(current.getData())
            current = current.getNext()

    def buscar_por_edad(self, edad):
        if self.__list is None:
            print("La lista está vacía.")
            return

        head = self.__list
        tail = self.__list
        while tail.getNext() is not None:
            tail = tail.getNext()

        head_diff = abs(head.getData().getEdad() - edad)
        tail_diff = abs(tail.getData().getEdad() - edad)

        found = False
        if head_diff <= tail_diff:
            current = head
            while current is not None:
                if current.getData().getEdad() == edad:
                    print(current.getData())
                    found = True
                current = current.getNext()
        else:
            current = tail
            while current is not None:
                if current.getData().getEdad() == edad:
                    print(current.getData())
                    found = True
                current = current.getPrev()

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