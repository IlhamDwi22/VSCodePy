n = int(input("n? "))
n = 2**n

def pascal_pattern(level):
    if level==1:
        return ["X"] # elementary triangle
    r = pascal_pattern(level//2) # get a triangle
    for i in range(len(r)): # copy the triangle...
        sep = " "*(level//2-len(r[i]))
        r.append(r[i]+sep+r[i]) # ...twice with separators
    return r

figure = pascal_pattern(n)

for l in figure:
    print(l)