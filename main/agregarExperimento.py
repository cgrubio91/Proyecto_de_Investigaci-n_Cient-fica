from datetime import datetime

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
    
    categorias = input('Ingrese la categoría del experimento:\nQuimica\nBiología\nFísica\n')
    
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

#if __name__ == "__main__":
#    listaExperimentos = []  # Crear una lista vacía para los experimentos
#    agregarExperimento(listaExperimentos)
#    
#    # Mostrar los experimentos para verificar
#    print("\nLista de experimentos:")
#    for exp in listaExperimentos:
#        print(f"Nombre: {exp.nombreExperimento} \nFecha del experimento: {exp.fechaExperimento.strftime('%d/%m/%Y')} \nCategoría: {exp.categorias} \nResultados: {exp.resultados}\n")

