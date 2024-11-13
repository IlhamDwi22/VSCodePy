def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

for i in range(0,11):   # a simple loop to test several calls
    print(f"{i}!={fact(i)}")