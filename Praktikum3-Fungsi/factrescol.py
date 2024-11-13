def fact_for_loop_rec(f,i,n):
    if i>n:
        return f
    return fact_for_loop_rec(f*i,i+1,n)

def fact_for_loop(n):
    return fact_for_loop_rec(1, 1,n)

for i in range(0,11):
    print(f"{i}!={fact_for_loop(i)}")