# Cantidad de casos
C = int(input())
for _ in range(C):
    # Solicitamos datos de entrada
    # M = participantes N = cantidad de Monedas
    # Monedas = denominación individual de cada moneda
    M, N = tuple(map(int,input().split(" ")))
    Monedas = tuple(map(int,input().split(" ")))

    max = sum(Monedas[::M])
    min = sum(Monedas[M-1::M])
    print(max - min)

