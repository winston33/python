from math import sqrt
from math import pow


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(pow(dx, 2) + pow(dy, 2))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(pow(dx, 2) + pow(dy, 2))


print(distance(0, 0, 3, 4))
print(Point(0, 0).distance(Point(3, 4)))
print(Point(0, 0).__eq__(Point(3, 0)))
print(Point(0, 0).__eq__(Point(0, 0)))
