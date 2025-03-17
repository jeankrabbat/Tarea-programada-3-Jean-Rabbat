from cola_prioridad_lista_enlazada import ColaPrioridad
from persona import Persona

def main():

    cola = ColaPrioridad()

    while True:
        print("\nMenu cola de prioridad:")
        print("1. Agregar una persona a la cola")
        print("2. Imprimir personas en la cola")
        print("3. Eliminar persona de la cola")
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
                cola.insercion(persona)
            except ValueError:
                print("Edad inválida. Por favor ingrese un número.")
        elif opcion == "2":
            cola.imprimir()
        elif opcion == "3":
            try:
                posicion = int(input("Ingrese la posicion a borrar: "))
                cola.eliminar(posicion)
            except ValueError:
                print("Posición inválida. Por favor ingrese un número.")
        elif opcion == "4":
            try:
                edad = int(input("Ingrese la edad de la persona a buscar: "))
                cola.buscar_por_edad(edad)
            except ValueError:
                print("Edad inválida. Por favor ingrese un número.")
        elif opcion == "5":
            nombre = input("Ingrese el nombre a buscar: ")
            cola.buscar_por_nombre(nombre)
        elif opcion == "6":
            apellido = input("Ingrese el apellido a buscar: ")
            cola.buscar_por_apellido(apellido)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else: 
            print("Ingreso una opcion no valida, por favor intentalo de nuevo")

if __name__ == "__main__":
    main()