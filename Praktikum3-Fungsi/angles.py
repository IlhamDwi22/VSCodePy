import math

def cosine_radian(a):
    "eats angles in radians"
    return math.cos(a)

def cosine_degree(a):
    "eats angles in radians"
    return math.cos(a/180*math.pi)

def cosine_gradian(a):
    "eats angles in radians"
    return math.cos(a/200*math.pi)


print(cosine_radian(math.pi/4))
print(cosine_degree(45))
print(cosine_gradian(50))