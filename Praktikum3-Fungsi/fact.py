def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

for i in range(0,11): # A simple loop to test several calls
    print(f"{i}!={fact(i)}")