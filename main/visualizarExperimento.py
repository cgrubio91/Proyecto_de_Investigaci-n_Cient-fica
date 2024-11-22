#Funcion para visualizar experimentos

def visualizarExperimentos (listaExperimentos):
    if not listaExperimentos:
        print ("No hay experimentos registrados")
        return
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}")
        print(f"Experimento: {experimento.nombreExperimento}")
        print(f"Fecha: {experimento.fechaExperimento.strfime('%d/%m/%Y')}")
        print(f"Categoria: {experimento.categorias}")
        print(f"Resultados: {experimento.resultados}")

        

 