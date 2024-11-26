#Función para comparar experimentos
import statistics
def compararExperimentos(listaExperimentos):
    if len(listaExperimentos) < 2:
        print("Se necesitan al menos 2 experimentos para realizar la comparacion")
        return
    
    #Mostramos la lista de experimentos
    print("\n Lista de Experimentos")
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {1}")
        print(f"{i}. {experimento.nombreExperimento}")
        
    #Solicitamos al usuario seleccionar experimentos a comparar
    try:
        seleccion = input("Seleccione los numeros de los experimentos a comparar separados por comas (por ejemplo: 1,2,3): ")
        indices = [int(i.strip())-1 for i in seleccion.split(",") if i.strip().isdigit()]

        #Validad seleccion
        if any(i < 0 or i >= len(listaExperimentos) for i in indices):
            print("Seleccion invalida. Intente nuevamente")
            return
        
        #Realizr comparacion
        print("\n Comparacion de Experimentos")
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
        print("\n Resultados de Comparacion")
        print(f"Mejor experimento: {mejor['nombre']} con un promedio de {mejor['promedio']:.2f}")
        print(f"Peor experimento: {peor['nombre']} con un promedio de {peor['promedio']:.2f}")
    except ValueError:
        print("Entrada invalida. Intente nuevamente.")
    

 #.split(",") Divide la cadena de texto en una lista de subcadenas usando coma (,) como separador
 #.strip() Elimina los espacios en blanco al inicio y al final de la cadena de {i}
 #.strip().isdigit() Este filtro comprueba si la cadena resultando de .strip() contiene solo digitos, asegurando que solo se procesen entradas validas
 # int(i.strip())-1 Convierte la cadena (Ya limpiada y validada en un numero entero con int(), luego le resta 1, esto por que los indices en Python inician desde 0
 #.2f se utiliza para mostrar un numero decimal con 2 cifras decimales, se controla como se presenta un numero flotante
 #         
    






