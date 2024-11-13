# computes approximations of pi
import math
v = 0
n = int(input('# of iterations, please:'))
for i in range(1, n+1):
    v = v + (1/i)**2
    pi_approx = math.sqrt(6*v)
    error = math.pi - pi_approx
    percent_error = abs(error/math.pi)*100
    if percent_error < 0.01:
        break   # no need to continue, goal is reached
print(f'After {i} iterations, pi approximation, equals to {pi_approx}')