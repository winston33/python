from math import pow
from math import sqrt

from geom_2d import *


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(pow(dx, 2) + pow(dy, 2))


print(distance(0, 0, 3, 4))
print(Point(0, 0).distance(Point(3, 4)))
print(Point(0, 0).__eq__(Point(3, 0)))
print(Point(0, 0).__eq__(Point(0, 0)))
