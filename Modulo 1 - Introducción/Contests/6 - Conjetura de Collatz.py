def Collatz(n):
    if n == 1:
        return "stop"
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1

n = int(input())
print(n)
while Collatz(n) != "stop":
    n = Collatz(n)
    print(n)
