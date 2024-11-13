# Binomial with a definition to compute n!

def fact(v):
    f = 1
    for i in range(1, v+1):
        f *= i
    return f

n = int(input("n="))
k = int(input("k="))

cnk = fact(n) // (fact(k) * fact(n-k))
print(f"C({n},{k})={cnk}")