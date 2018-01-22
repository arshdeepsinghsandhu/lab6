class Point():
    x = 0
    y = 0
class Rectangle(object):
    width = 0
    height = 0
box = Rectangle()
box.corner = Point()
box.width = 10
box.height = 20
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

def print_point(p):
    print (p.x , p.y)

center = find_center(box)

print_point(center)