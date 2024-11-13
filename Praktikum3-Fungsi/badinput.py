def inverse(x):
    if x == 0:
        print("Wrong parameter")
        quit()
    return 1/x

v = int(input("Give me a value:"))
print(inverse(v))