def inverse(x):
    if x==0:
        return None
    return 1/x

v = int(input("Give me a value: "))
inverse_v = inverse(v)
if inverse_v == None:
    print("Something's wrong, fallback to...")
else:
    print(inverse_v)