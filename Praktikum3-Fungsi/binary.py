def binary_rep(n):
    if n<2:
        return "0" if n==0 else "1"
    return binary_rep(n//2) + ("0" if n%2==0 else "1")


print(binary_rep(int(input("n? "))))