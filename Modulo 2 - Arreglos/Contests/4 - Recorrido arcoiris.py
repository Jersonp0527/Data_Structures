N = int(input())
caso = tuple(input().split(", "))
result = tuple()
rango = N
for i in range(N//2):
    result = result + tuple(caso[i]) + tuple(caso[N-i-1])
if N % 2 != 0:
    result = result + tuple(caso[N//2])
result = "".join(result)
print(result)

