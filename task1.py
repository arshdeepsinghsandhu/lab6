import math
class Point():
    """represents the point in 2-D space"""
    x=0
    y=0
p1 = Point()
p1.x = 3
p1.y = 3
p2 = Point()
p2.x = 5
p2.y = 5

def distance_between_points(p1,p2):
    distance = math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    return (distance)


print(distance_between_points(p1,p2))