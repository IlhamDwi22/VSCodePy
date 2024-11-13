# computes approximations of pi
import math
v = 0
n = int(input('# of iterations, please:'))
while n < 0:
    print('Bad input, positive or 0 please.')
    n = int(input('# of iterations, please:'))
for i in range(1, n+1):
    v = v + (1/i)**2
pi_approx = math.sqrt(6*v)
print(f'After {n} iterations, pi approx. equals to {pi_approx}')