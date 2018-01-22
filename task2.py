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



def move_rectangle(rect, dx, dy):
    rect.corner.x = rect.corner.x + dx
    rect.corner.y = rect.corner.y + dx
    return rect.corner.x , rect.corner.y


def print_point(p):
    print (p.x , p.y)

#center = find_center(box)

print(move_rectangle(box, 5.0, 5.0))

#print_point(center)