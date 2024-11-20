def menu():
    listaExperimentos = []
    while True:
        print("\nMenú de opciones")
        print("1. Agregar experimento: ")
        print("2. Ver experimentos: ")
        print("3. Analizar experimentos: ")
        print("4. Generar informe: ")
        print("5. Salir")

        opcion = int(input('\nSeleccione el numero de su selección\n '))
        if opcion == 1:
            agregarExperimento(listaExperimentos)
        elif opcion == 2:
            verExperimentos(listaExperimentos)
        elif opcion == 3:
            analizarExperimentos(listaExperimentos)
        elif opcion == 4:
            generarInforme(listaExperimentos)
        elif opcion == 5:
            print('Saliendo del programa...')
            break
        else:
            print("Opción invalida")