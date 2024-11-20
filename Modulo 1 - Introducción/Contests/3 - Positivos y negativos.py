# Positivos
Q = 0
# Negativos
R = 0
for i in range(int(input())):
    n = int(input())
    if n < 0:
        R += n
    else:
        Q += n
print(f"positivos {Q}, negativos {R}")
