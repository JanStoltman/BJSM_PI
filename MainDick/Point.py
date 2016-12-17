import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def proximity(self, point2):

        return math.sqrt((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)