import math

def cosine(angle,unit):
    if unit == 1:
        return math.cos(angle)
    if unit == 2:
        return math.cos(angle/180*math.pi)
    if unit == 3:
        return math.cos(angle/200*math.pi)
    print("error")
    quit()

print(cosine(unit=3,angle=50))