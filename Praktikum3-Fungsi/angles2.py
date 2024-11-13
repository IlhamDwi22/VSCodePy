import math

def cosine(angle,unit=1):
    "cosine of the angle expressed in radians (1), degrees (2), gradians (3)"
    if unit == 1:
        return math.cos(angle)
    if unit == 2:
        return math.cos(angle/180*math.pi)
    if unit == 3:
        return math.cos(angle/200*math.pi)
    print("Bad unit for angle")
    quit()
    
print(cosine(math.pi/4))
print(cosine(45,2))
print(cosine(50,3))