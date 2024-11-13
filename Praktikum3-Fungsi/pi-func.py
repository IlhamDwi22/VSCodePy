# computes approximations of pi
import math

def approx_pi(n):
    v = 0
    for i in range(1,n+1):
        v = v + (1/i)**2
    return math.sqrt(6*v)

def get_value_from_user():
    n = int(input('# of iterations, please:'))
    n_inputs = 1
    while n < 0:
        if n_inputs < 3:    # try at most 3 times
            print('Bad input, positive or 0 please.')
            n = int(input('# of iterations, please:'))
            n_inputs += 1   # one more user input
        else: # no good input, default value then
            print('Too many bad inputs. Now using a default value.')
            n = 10
    return n

n = get_value_from_user()
pi_approx = approx_pi(n)
print(f'After {n} iterations, pi approximatively equals to {pi_approx}')
