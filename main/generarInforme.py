from datetime import datetime

def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print('No hay experimentos registrados')
        return
    
# Abrir un archivo txt para escribir el informe
    with open("Informe_experimentos.txt", "w") as archivo:
        archivo.write('*** INFORME DE EXPERIMENTOS ***\n\n')
        archivo.write('+' * 40 + '\n\n')
        # Escribir los detalles del archivo txt
        for i, experimento in enumerate (listaExperimentos, 1):
            archivo.write(f'Nombre del experimento: {experimento.nombreExperimento}\n')
            archivo.write(f'Fecha del experimento: {experimento.fechaExperimento.strftime("%d/%m/%Y")}\n')
            archivo.write(f'Categoría: {experimento.categorias}\n')
            archivo.write(f'Resultados: {experimento.resultados}\n\n')
            archivo.write('+' * 40 + '\n\n')
        conclusiones = input('¿Tienes conclusiones generales para el informe?\n')
        if conclusiones.strip():
            archivo.write(f'Conclusiones: {conclusiones}\n')

    print("Informe generado como 'informe de experimentos'")

if __name__ == "__main__":
    listaExperimentos = []  # Crear una lista vacía para los experimentos
    generarInforme(listaExperimentos)