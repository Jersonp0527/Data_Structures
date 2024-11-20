# Convertir lista de Str a int
def toNum(Lista):
    return list(map(int, Lista))

# Declarar Variables
N1 = int(input())
L1 = input().split(" ")
L1 = toNum(L1)
N2 = int(input())
L2 = input().split(" ")
L2 = toNum(L2)

# Convertir L1 a diccionario para búsquedas rápidas
L1_dict = {value: index + 1 for index, value in enumerate(L1)}

# Calcular Total
Total = 0
for num in L2:
    # Si L2 en la posición i está en el diccionario L1
    if num in L1_dict:
        # Sumo el índice almacenado en el diccionario al total
        Total += L1_dict[num]

print(Total)

