import sys

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

sys.setrecursionlimit(3000)
for i in range(2000,2300):
    print(f"{i}!={fact(i)}")