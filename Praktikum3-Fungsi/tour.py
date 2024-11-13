import random

def tournament_aux(l, begin, end):
    if begin==end-1:
        return l[begin], l[begin]
    mid = (begin+end)//2
    min, max = tournament_aux(l, begin, mid)
    minr, maxr = tournament_aux(l, mid, end)
    if min > minr:
        min = minr
    if max < maxr:
        max = maxr
    return min, max

def tournament(l):
    if len(l)==0:
        return None, None
    return tournament_aux(l, 0, len(l))

l = [random.randint(0,100) for i in range(20)]
print(l)
print(tournament(l))