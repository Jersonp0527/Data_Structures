"""
Un grafo no dirigido se considera bipartito si sus nodos 
o vértices pueden repartirse en dos conjuntos disjuntos A y B de tal
forma que todas las aristas o arcos tengan un extremo en A y el otro en B.
Visto de manera gráfica, en un grafo bipartito todos sus nodos pueden 
pintarse con dos colores de tal forma que no exista ninguna arista que 
conecte dos nodos del mismo color.

Input
La entrada comienza con una línea que contiene la cantidad C de casos de prueba,
no más de 50. Cada caso de prueba comienza con una línea que contiene dos valores 
separados entre sí por un espacio en blanco: la cantidad N de nodos (1 ≤ N ≤ 200)
y la cantidad M de aristas (0 ≤ M ≤ N(N-1)/2). Luego siguen M líneas, cada una
con dos valores u, v separados entre sí por una coma y un espacio en blanco
(1 ≤ u < v ≤ N). Cabe recordar que, siendo un grafo no dirigido,
la arista u -> v implica la existencia de la arista v -> u.

Output
La salida debe contener C líneas, cada una con el mensaje (sin comillas)
'bipartito' o 'no bipartito' según sea el caso.
"""
from collections import deque

def BFS(grafo, nodo, visitados):
    # Creamos la cola y agregamos el nodo
    cola = deque()
    cola.append(nodo)
    # Marcamos el nodo como visitado
    visitados[nodo] = 1
    # Mientras la cola tenga elementos
    while cola:
        # Sacamos el nodo de la cola
        nodo = cola.popleft()
        # Recorremos a los vecinos del nodo
        for vecino in grafo[nodo]:
            # Si el vecino no ha sido visitado
            if visitados[vecino] == 0:
                # Marcamos el vecino como visitado
                visitados[vecino] = -visitados[nodo]
                # Agregamos el vecino
                cola.append(vecino)
            # Si el vecino ya fue visitado
            elif visitados[vecino] == visitados[nodo]:
                return False
    return True

C = int(input())
for _ in range(C):
    # grafo = {nodo: [vecinos]}
    grafo = {}
    # Leemos la cantidad de nodos y aristas
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split(', '))
        if a not in grafo:
            grafo[a] = []
        if b not in grafo:
            grafo[b] = []
        grafo[a].append(b)
        grafo[b].append(a)
    
    # Inicializamos la lista de visitados
    visitados = [0] * (N + 1)
    # Recorremos los nodos
    for nodo in grafo:
        if visitados[nodo] == 0:
            if not BFS(grafo, nodo, visitados):
                print('no bipartito')
                break
    else:
        print('bipartito')
