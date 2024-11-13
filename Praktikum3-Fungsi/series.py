import math

def e_approx(n):
    e = 0
    for i in range(0,n+1):
        e += 1/math.factorial(i)
    return e

def pi_approx(n):
    v = 0
    for i in range(1,n+1):
        v = v + (1/i)**2
    return math.sqrt(6*v)