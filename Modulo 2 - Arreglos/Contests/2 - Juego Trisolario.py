N = int(input())
So = tuple(map(int, input().split(", ")))
Lar = tuple(map(int, input().split(", ")))
Is = tuple(map(int, input().split(", ")))
puntosSo = 0
puntosLar = 0
puntosIs = 0
status = "null"
for i in range(N):
    if (So[i] + Lar[i] + Is[i]) % 2 == 0:
        status = "par"
    else:
        status = "impar"
    if So[i] % 2 == 0 and status == "par":
        puntosSo += 1
    elif So[i] % 2 != 0 and status == "impar":
        puntosSo += 1
    if Lar[i] % 2 == 0 and status == "par":
        puntosLar += 1
    elif Lar[i] % 2 != 0 and status == "impar":
        puntosLar += 1
    if Is[i] % 2 == 0 and status == "par":
        puntosIs += 1
    elif Is[i] % 2 != 0 and status == "impar":
        puntosIs += 1
print(f"SO:{puntosSo}, LAR:{puntosLar}, IS:{puntosIs}")
