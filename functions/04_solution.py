# function that return both area and parimeter of the give radius
import math
def Area(n):
    area = 2 * math.pi * n
    paramter = math.pi* (n**2)
    return round(area),round(paramter)
     
print(Area(7))