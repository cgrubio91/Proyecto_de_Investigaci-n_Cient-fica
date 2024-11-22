#Función para calcular estadísticas básicas
#importamos "statistics" ya que es una libreria estandar que proporciona funciones para realizar calculos estadisticos basicos sobre datos numericos

import statistics

def calcularEstadisticas(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados")
        return
    for experimento in listaExperimentos:
        #Usamos statistics.mean() ya que nos calcula especificamente el promedio
        promedio = statistics.mean(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)
        print(f"\nAnalisis de {experimento.resultados}")
        print(f"El promedio de los resultados es: {promedio}")
        print(f"Valor maximo de los resultados: {maximo}")
        print(f"Valor minimo de los resultados: {minimo}")

    

