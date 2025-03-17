from lista_enlazada_ordenada import Lista_enlazada
from persona import Persona

def main():

    lista = Lista_enlazada()

    while True:
        print("\nMenu lista enlazada:")
        print("1. Agregar una persona a la lista")
        print("2. Imprimir personas almacenadas en la lista")
        print("3. Borrar persona de la lista")
        print("4. Buscar persona por edad")
        print("5. Buscar persona por nombre")
        print("6. Buscar persona por apellido")
        print("7. Salir del programa")

        opcion = input("Seleccione una de las opciones: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido1 = input("Ingrese el primer apellido: ")
            apellido2 = input("Ingrese el segundo apellido: ")
            try:
                edad = int(input("Ingrese la edad: "))
                persona = Persona(nombre, apellido1, apellido2, edad)
                lista.insercion(persona)
            except ValueError:
                print("Edad inválida. Por favor ingrese un número.")
        elif opcion == "2":
            lista.imprimir()
        elif opcion == "3":
            try:
                posicion = int(input("Ingrese la posicion a borrar: "))
                lista.eliminar(posicion)
            except ValueError:
                print("Posición inválida. Por favor ingrese un número.")
        elif opcion == "4":
            try:
                edad = int(input("Ingrese la edad de la persona a buscar: "))
                lista.buscar_por_edad(edad)
            except ValueError:
                print("Edad inválida. Por favor ingrese un número.")
        elif opcion == "5":
            nombre = input("Ingrese el nombre a buscar: ")
            lista.buscar_por_nombre(nombre)
        elif opcion == "6":
            apellido = input("Ingrese el apellido a buscar: ")
            lista.buscar_por_apellido(apellido)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else: 
            print("Ingreso una opcion no valida, por favor intentalo de nuevo")

if __name__ == "__main__":
    main()