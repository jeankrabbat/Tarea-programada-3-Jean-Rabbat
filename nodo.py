class nodo:
    # Lista enlazada
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def setNext(self, next_node):
        self.__next = next_node

    def getNext(self):
        return self.__next
    
    def getData(self):
        return self.__data

    def __str__(self):
        return f"Data: {self.__data}"