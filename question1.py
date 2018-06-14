from math import pi
def areaOfCircle(radius):
    if type(radius)  == int:
        areaa = pi * (radius ** 2)
        print (areaa)
    else :
        print ("wrong input")

areaOfCircle(2)