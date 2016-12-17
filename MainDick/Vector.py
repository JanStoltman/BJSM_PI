from MainDick.Point import Point
from math import radians, sin, cos

class Vector:

    def __init__(self, X, Y):
        self.X = int(X)
        self.Y = int(Y)
        

    def sum(self, vector2):
        self.X += vector2.X
        self.Y += vector2.Y

        return self


    def multiply(self, scalar):
        self.X *= scalar
        self.Y *= scalar

        return self


    def magnitude(self):
        point = Point(self.X, self.Y)
        return Point(0, 0).proximity(point)


    def to_list(self):
        return [self.X, self.Y]

    def from_len_ang_angle(self, len, angle):
        return Vector(len * sin(radians(angle)), len * cos(radians(angle)))