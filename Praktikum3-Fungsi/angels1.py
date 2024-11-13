import math

def cosine(angle,unit):
    """unit: 1: radians, 2: degrees, 3:gradians"""
    if unit == 1:
        return math.cos(angle)
    if unit == 2:
        return math.cos(angle/180*math.pi)
    if unit == 3:
        return math.cos(angle/200*math.pi)
    print("Bad unit for angle")
    quit()
    
print(cosine(math.pi/4,1))
print(cosine(45,2))
print(cosine(50,3))