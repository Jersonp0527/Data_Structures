# Convertir lista de Str a int
def toNum(Lista):
# input ["1","2","3"]
# output [1,2,3]
    for i in range(len(Lista)):
        Lista[i] = int(Lista[i])
    return Lista

# Declarar Variables
N1 = int(input())
L1 = input().split(" ")
L1 = toNum(L1)
N2 = int(input())
L2 = input().split(" ")
L2 = toNum(L2)

# Calcular Total
Total = 0
for i in range(N2):
    # Si L2 en la pisición i está en L1
    if L2[i] in L1:
        # Sumo el indice dónde se encuentra al total + 1
        Total += L1.index(L2[i]) + 1
print(Total)

