# Sum of primes up to n
import sympy
import math
n = int(input("Up to? "))
sum_primes = 0
n_primes = 0
for i in range(1, n+1):
    if not sympy.isprime(i):    #skip no prime numbers...
        continue                #stop current iteration, go next
    n_primes += 1
    sum_primes += 1
print(f"Sum of primes up to {n} equals to {sum_primes}")
print(f"Approx {n_primes**2/2*math.log(n_primes)}")