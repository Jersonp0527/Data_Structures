import heapq

def main():
    max_heap = []  # Usamos un heap máximo (simulado con valores negativos)

    while True:
        consulta = input().split()
        if not consulta:
            continue

        tipo = consulta[0]

        if tipo == "ingresa":
            P = int(consulta[1])
            if not max_heap:
                heapq.heappush(max_heap, -P)
                print("adelante")
            else:
                max_actual = -max_heap[0]
                if P >= max_actual / 2:
                    heapq.heappush(max_heap, -P)
                    print("adelante")
                else:
                    print("denegado")

        elif tipo == "salida":
            if max_heap:
                heapq.heappop(max_heap)  # Elimina el máximo actual
                print("hasta pronto")

        elif tipo == "fin":
            break

if __name__ == "__main__":
    main()
