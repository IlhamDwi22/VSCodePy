# Binomial (with cut-n-paste)

n = int(input("n="))
k = int(input("k="))

n_fact = 1          # n!
for i in range(1,n+1):
    n_fact *= i
    
k_fact = 1          # k!
for i in range(1,n+1):
    k_fact *= i

nk_fact = 1          # (n-k)!
for i in range(1,n-k+1):
   nk_fact *= i

cnk = n_fact//(k_fact*nk_fact)
print(f"C({n},{k})={cnk}")