# computes approximations of pi
import math
v = 0
n = int(input('# of iterations, please:'))
i = 1
pi_approx = math.sqrt(6*v)
error = math.pi - pi_approx
percent_error = abs(error/math.pi)*100
while i < n+1 and percent_error >= 0.01:
    v = v + (1/i)**2
    pi_approx = math.sqrt(6*v)
    error = math.pi - pi_approx
    percent_error = abs(error/math.pi)*100
    i += 1
print(f'After {i} iterations, pi approx. equals to {pi_approx}')