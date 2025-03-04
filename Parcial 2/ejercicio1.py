# Diccionario para contar la cantidad de productos por equipo
diccCant = {}

# Diccionario para almacenar los productos únicos por equipo
diccSet = {}

# Bucle infinito para leer las entradas del usuario
while(1):
    line = input()  # Leer una línea de entrada
    
    if(line == '#'):
        break  # Si la línea es '#', salir del bucle
    
    # Dividir la línea en equipo (eq), agente (ag) y producto (pr)
    eq, ag, pr = line.split()
    
    # Incrementar el contador de productos para el equipo
    diccCant[eq] = diccCant.get(eq, 0) + 1
    
    # Inicializar el conjunto de productos para el equipo si no existe
    diccSet[eq] = diccSet.get(eq, set())
    
    # Agregar el producto al conjunto de productos del equipo
    diccSet[eq].add(pr)
    
# Iterar sobre los equipos y sus conjuntos de productos
for eq, pres in diccSet.items():
    # Si el equipo tiene 3 o más productos únicos, imprimir el equipo y su contador de productos
    if(len(pres) >= 3):
        print(eq, diccCant[eq])