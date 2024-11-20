c = int(input())
a = tuple()
b = tuple()
for _ in range(c):
    result = tuple()
    case = tuple(input().split(" "))
    case = case[::-1]
    a = case[::2]
    b = case[1::2]
    for i in range(len(case)//2):
        result = result + tuple(b[i]) + tuple(a[i])
    if len(case) % 2 != 0:
        result = result + tuple(a[len(case)//2])
    result = "".join(result)
    print(result)

