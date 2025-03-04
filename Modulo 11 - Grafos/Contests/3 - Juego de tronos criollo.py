def visitar_nodo(G, nodo, visitados):
    """Función auxiliar para realizar una búsqueda en profundidad (DFS) en el grafo.

    Args:
        G (dict): diccionario que representa el grafo.
        nodo (int): nodo actual.
        visitados (set): conjunto de nodos visitados.
    """
    # Crear una pila para la DFS
    pila = [nodo]
    while pila:
        actual = pila.pop()
        if actual not in visitados:
            visitados.add(actual)
            # Añadir los vecinos no visitados a la pila
            for vecino in G[actual]:
                if vecino not in visitados:
                    pila.append(vecino)

# Función para contar el número de familias
def familias(G):
    """Esta función cuenta el numero de familias que hay en un grafo
    pasando por cada nodo del grafo y contando los subgrafos

    Args:
        G (dict): diccionario que almacena las relaciones familiares
        
    Returns:
        int: numero de familias
    """
    # Inicializar el contador de familias
    familias = 0
    # Inicializar el conjunto de nodos visitados
    visitados = set()
    # Recorrer cada nodo del grafo
    for nodo in G:
        # Si el nodo no ha sido visitado
        if nodo not in visitados:
            # Aumentar el contador de familias
            familias += 1
            # Llamar a la función que visita los nodos
            visitar_nodo(G, nodo, visitados)
    return familias

# Funcion para encontrar la familia con mas personas
def familia_mas_grande(G):
    """Función que encuentra la familia con más personas, donde cada familia
    es un subgrafo del grafo original.

    Args:
        G (dict): diccionario que almacena las relaciones familiares
        
    Returns:
        int: numero de personas en la familia más grande
    """
    # Inicializar el contador de personas en la familia más grande
    max_personas = 0
    # Inicializar el conjunto de nodos visitados
    visitados = set()
    # Recorrer cada nodo del grafo
    for nodo in G:
        # Si el nodo no ha sido visitado
        if nodo not in visitados:
            # Inicializar el contador de personas en la familia actual
            personas = 0
            # Crear una pila para la DFS
            pila = [nodo]
            while pila:
                actual = pila.pop()
                if actual not in visitados:
                    visitados.add(actual)
                    # Añadir los vecinos no visitados a la pila
                    for vecino in G[actual]:
                        if vecino not in visitados:
                            pila.append(vecino)
                    # Aumentar el contador de personas
                    personas += 1
            # Actualizar el contador de personas en la familia más grande
            max_personas = max(max_personas, personas)
    return max_personas

# Numero de casos
C = int(input())
for _ in range(C):
    # Crear el diccionario de conexiones
    G = {}
    # Registros de parentesco
    R = int(input())
    for _ in range(R):
        # Leer los dos datos
        a, b = map(int, input().split())
        # almacenar en el grafo la conexión
        if a not in G:
            G[a] = []
        if b not in G:
            G[b] = []
        G[a].append(b)
        G[b].append(a)
    
    # Imprimir el numero de familias y la cantidad de integrantes de la familia mas grande
    print(familias(G), familia_mas_grande(G))
