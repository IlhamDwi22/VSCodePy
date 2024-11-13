import series

def get_user_input():
    n = int(input('# of iterations, please:'))
    n_inputs = 1
    while n < 0:
        if n_inputs < 3:    # try at most 3 times
            print('Bad input, positive or 0 please.')
            n = int(input('# of iterations, please:'))
            n_inputs += 1   # one more user input
        else:   # no good input, default value then
            print('Too many bad inputs. Now using a default value.')
            n = 10
    return n

n = get_user_input()
print(f"{n}-th approximation of pi is {series.pi_approx(n)}")
print(f"{n}-th approximation of e is {series.e_approx(n)}")