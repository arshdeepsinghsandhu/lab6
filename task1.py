#def distance_between_points(x,y)
import math
class Point(object):
    """represents the point in 2-D space"""
blank = Point()
blank.x = 3.0
blank.y = 4.0
x = blank.x
y = blank.y
distance = math.sqrt(x**2 + y**2)


print (x,y)

print (distance)
