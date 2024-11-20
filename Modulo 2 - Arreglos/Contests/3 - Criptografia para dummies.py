c = int(input())
a = tuple()
b = tuple()
result = tuple()
for _ in range(c):
    case = tuple(input().split(" "))
    case = case[::-1]
    a = case[::2]
    b = case[1::2]
    for i in range(len(case)//2):
        result = result + tuple(b[i]) + tuple(a[i])
    print(result)

