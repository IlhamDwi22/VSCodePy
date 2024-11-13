# computes approximations of pi
import math
v = 0
n = int(input('# of iterations, please:'))
for i in range(1, n+1):
    v = v + (1/i)**2
print('After', n,'iterations, approx. of pi is', math.sqrt(6*v))