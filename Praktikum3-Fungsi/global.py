my_var = 10
def f():
    global my_var
    my_var += 1
    
print(my_var)
f()
print(my_var)