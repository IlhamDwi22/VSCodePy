# computes approximations of pi
import math
i = 0               # approximation index
v = 0               # first approximation
print(i, math.sqrt(6*v))
i = i + 1           # next approx
v = v + (1/i)**2    # add one more term
print(i, math.sqrt(6*v))
i = i + 1           # next approx
v = v + (1/i)**2    # add one more term
print(i, math.sqrt(6*v))
# to be continued...