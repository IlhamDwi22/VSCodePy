# computes approximations of pi
import math
v = 0
for i in range(1,10001):
    v = v + (1/i)**2
    print(i, math.sqrt(6*v))