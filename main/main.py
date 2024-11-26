from datetime import datetime
import statistics
#Creacion de diccionario con las categorias del programa, lo usamos para mostrar la categoria
CATEGORIAS = {
    "1": "Química",
    "2": "Biología",
    "3": "Física"
}

class Experimento:
    def __init__(self, nombreExperimento, fechaExperimento, categorias, resultados):  # método constructor
        self.nombreExperimento = nombreExperimento
        self.fechaExperimento = fechaExperimento
        self.categorias = categorias
        self.resultados = resultados

# Función para agregar una experimento
def agregarExperimento(listaExperimentos):
    nombreExperimento = input('Ingrese el nombre del experimento: ')
    fechaExperimento_str = input('Ingrese la fecha del experimento (DD/MM/AAAA): ')
    try:
        fechaExperimento = datetime.strptime(fechaExperimento_str, '%d/%m/%Y')
    except ValueError:
        print('Fecha no válida. Intente nuevamente.')
        return
    
    categorias = input('Ingrese la categoría del experimento:\n1. Quimica\n2. Biología\n3. Física\n¿Cual desea seleccionar?\n')
    if categorias not in CATEGORIAS:
        print("Categoría no valida. Intente nuevamente")
        return
    
    resultados_str = input('Ingrese los resultados (separe con comas si son varias): ')
    try:
        resultados = list(map(float, resultados_str.split(',')))
    except ValueError:
        print('Formato de resultados no válido')
        return

    # Crear un objeto Experimento y agregarlo a la lista de experimentos
    experimento = Experimento(nombreExperimento, fechaExperimento, categorias, resultados)
    listaExperimentos.append(experimento)
    print('Experimento agregado con éxito')

def compararExperimentos(listaExperimentos):
    if len(listaExperimentos) < 2:
        print("Se necesitan al menos 2 experimentos para realizar la comparación")
        return
    
    #Mostramos la lista de experimentos
    print("\n Lista de Experimentos")
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}")
        print(f"{i}. {experimento.nombreExperimento}")
        
    #Solicitamos al usuario seleccionar experimentos a comparar
    try:
        seleccion = input("Seleccione los números de los experimentos a comparar separados por comas (por ejemplo: 1,2,3): ")
        indices = [int(i.strip())-1 for i in seleccion.split(",") if i.strip().isdigit()]

        #Validar seleccion
        if any(i < 0 or i >= len(listaExperimentos) for i in indices):
            print("Seleccion invalida. Intente nuevamente")
            return
        
        #Realizar comparacion
        print("\n Comparación de Experimentos")
        mejoreResultados = []
        for i in indices:
            experimento = listaExperimentos[i]
            promedio = statistics.mean(experimento.resultados) if experimento.resultados else 0
            maximo = max(experimento.resultados) if experimento.resultados else 0
            minimo = min(experimento.resultados) if experimento.resultados else 0
            mejoreResultados.append({
                "nombre": experimento.nombreExperimento,
                "promedio": promedio,
                "maximo": maximo,
                "minimo": minimo,
            })
            print(f"\n{experimento.nombreExperimento}")
            print(f"Resultados: {experimento.resultados}")
            print(f"Promedio: {promedio:.2f}, Maximo: {maximo:.2f}, Minimo: {minimo:.2f}")

        #Identificar mejor y peor experimento
        mejor = max(mejoreResultados, key=lambda x: x["promedio"])
        peor = min(mejoreResultados, key=lambda x: x["promedio"])
        print("\nResultados de Comparacion\n")
        print(f"Mejor experimento: {mejor['nombre']} con un promedio de {mejor['promedio']:.2f}")
        print(f"Peor experimento: {peor['nombre']} con un promedio de {peor['promedio']:.2f}")
    except ValueError:
        print("Entrada invalida. Intente nuevamente.")

def calcularEstadisticas(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados")
        return
    for experimento in listaExperimentos:
        #Usamos statistics.mean() ya que nos calcula especificamente el promedio
        promedio = statistics.mean(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)
        print(f"\nAnalisis de {experimento.nombreExperimento}")
        print(f"El promedio de los resultados es: {promedio}")
        print(f"Valor maximo de los resultados: {maximo}")
        print(f"Valor minimo de los resultados: {minimo}")

def visualizarExperimentos (listaExperimentos):
    if not listaExperimentos:
        print ("No hay experimentos registrados")
        return
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}")
        print(f"Experimento: {experimento.nombreExperimento}")
        print(f"Fecha: {experimento.fechaExperimento.strftime('%d/%m/%Y')}")
        print(f"Categoria: {CATEGORIAS.get(experimento.categorias, 'Desconocida')}")
        print(f"Resultados: {experimento.resultados}")

def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print('No hay experimentos registrados')
        return
    
# Abrir un archivo txt para escribir el informe
    with open("Informe_experimentos.txt", "w", encoding="utf-8") as archivo:
        archivo.write('*** INFORME DE EXPERIMENTOS ***\n\n')
        archivo.write('*' * 40 + '\n\n')
        # Escribir los detalles del archivo txt
        for i, experimento in enumerate (listaExperimentos, 1):
            archivo.write(f'Nombre del experimento: {experimento.nombreExperimento}\n')
            archivo.write(f'Fecha del experimento: {experimento.fechaExperimento.strftime("%d/%m/%Y")}\n')
            archivo.write(f"Categoría: {CATEGORIAS.get(experimento.categorias, 'Desconocida')}\n")
            archivo.write(f'Resultados: {experimento.resultados} \n\n')
            archivo.write('-' * 40 + '\n\n')
        conclusiones = input('¿Tienes conclusiones generales para el informe?\n')
        if conclusiones.strip():
            archivo.write(f'Conclusiones: {conclusiones}\n\n')
            archivo.write('*' * 40 + '\n\n')
            archivo.write(f'Autores:\nCristian Rubio\nWendy Torres\n')

    print("Informe generado como 'Informe_experimentos.txt'")

def menu():
    listaExperimentos = []
    while True:
        print("\nMenú de opciones")
        print("1. Agregar experimento: ")
        print("2. Ver experimentos: ")
        print("3. Analizar experimentos: ")
        print("4. Generar informe: ")
        print("5. Comparar experimentos: ")
        print("6. Salir")

        opcion = int(input('\nSeleccione el numero de su selección\n '))
        if opcion == 1:
            agregarExperimento(listaExperimentos)
        elif opcion == 2:
            visualizarExperimentos(listaExperimentos)
        elif opcion == 3:
            calcularEstadisticas(listaExperimentos)
        elif opcion == 4:
            generarInforme(listaExperimentos)
        elif opcion == 5:
            compararExperimentos(listaExperimentos)
        elif opcion == 6:
            print('Saliendo del programa...')
            break
        else:
            print("Opción invalida")

if __name__== "__main__":
    menu()