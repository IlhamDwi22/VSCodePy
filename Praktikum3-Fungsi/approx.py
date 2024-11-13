import math

def e_approx(n):
    e = 0
    for i in range(0,n+1):
        e += 1/math.factorial(i)
    return e