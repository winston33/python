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
