def special_print(l):
    for i in range(len(l)):
        print(' ' if l[i]==0 else 'X',end='')
    print()

def next_pascal_mod_2(l):
    return [1]+[(l[i]+l[i+1])%2 for i in range(len(l)-1)]+[1]

def pascal_mod_2_aux(l,level):
    if level==0:
        return
    special_print(l)
    pascal_mod_2_aux(next_pascal_mod_2(l),level-1)

def pascal_mod_2(level):
    pascal_mod_2_aux([1],level)

pascal_mod_2(int(input("n? ")))