import math

class Point:

    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def proximity(self, point2):

        return math.sqrt((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)