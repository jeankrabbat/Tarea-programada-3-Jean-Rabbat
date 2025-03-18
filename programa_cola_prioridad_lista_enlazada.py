from cola_prioridad_lista_enlazada import ColaPrioridad
from persona import Persona

def main():

    cola = ColaPrioridad()

    while True:
        print("\nMenu cola de prioridad:")
        print("1. Agregar una persona a la cola")
        print("2. Imprimir personas en la cola")
        print("3. Sacar persona de la cola")
        print("4. Salir del programa")

        opcion = input("Seleccione una de las opciones: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido1 = input("Ingrese el primer apellido: ")
            apellido2 = input("Ingrese el segundo apellido: ")
            try:
                edad = int(input("Ingrese la edad: "))
                persona = Persona(nombre, apellido1, apellido2, edad)
                cola.enqueue(persona)
            except ValueError:
                print("Edad inválida. Por favor ingrese un número.")
        elif opcion == "2":
            cola.imprimir()
        elif opcion == "3":
            cola.dequeue()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else: 
            print("Ingreso una opcion no valida, por favor intentalo de nuevo")

if __name__ == "__main__":
    main()