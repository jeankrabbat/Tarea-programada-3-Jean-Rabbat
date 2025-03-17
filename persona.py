class Persona:
    
    def __init__(self,nombre,apellido1,apellido2,edad):
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__edad = edad

    def getNombre(self):
        return self.__nombre

    def getApellido1(self):
        return self.__apellido1

    def getApellido2(self):
        return self.__apellido2

    def getEdad(self):
        return self.__edad

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido1(self, apellido1):
        self.__apellido1 = apellido1

    def setApellido2(self, apellido2):
        self.__apellido2 = apellido2

    def setEdad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f"{self.__nombre} {self.__apellido1} {self.__apellido2}, Edad: {self.__edad}"
        