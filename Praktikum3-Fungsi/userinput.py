def get(max_input,default_value):
    n = int(input('# of iterations, please:'))
    n_inputs = 1
    while n < 0:
        if n_inputs < max_input: # try at most 3 times
            print('Bad input, positive or 0 please.')
            n = int(input('# of iterations, please:'))
            n_inputs += 1 # one more user input
        else: # no good input, default value then
            print('Too many bad inputs. Now using a default value.')
            n = default_value
    return n