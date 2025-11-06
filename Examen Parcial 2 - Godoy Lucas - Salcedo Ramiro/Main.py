from Funciones import agregar_celular, mostrar_todos, buscar_un_modelo, eliminar, mostrar_menu

def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            agregar_celular()
        elif opcion == "2":
            mostrar_todos()
        elif opcion == "3":
            buscar_un_modelo()
        elif opcion == "4":
            eliminar()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Probá otra vez.")

if __name__ == "__main__":
    main()