N = int(input())
List = tuple(map(int, input().split()))
sum = 0
for i in range(N - 1, -1, -1):
    if i == N - 1:
        sum += List[i]
        continue
    sum += List[i]
    print(sum)
