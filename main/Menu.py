def menu():
    listaTareas = []
    while True:
        print("\nMenú de opciones")
        print("1. Agregar experimento: ")
        print("2. Ver experimentos: ")
        print("3. Analizar experimentos: ")
        print("4. Generar informe: ")
        print("5. Salir")

        opcion = int(input('\nSeleccione el numero de su selección\n '))
        if opcion == 1:
            agregarExperimento(listaTareas)
        elif opcion == 2:
            verExperimentos(listaTareas)
        elif opcion == 3:
            analizarExperimentos(listaTareas)
        elif opcion == 4:
            generarInforme(listaTareas)
        elif opcion == 5:
            print('Saliendo del programa...')
            break
        else:
            print("Opción invalida")