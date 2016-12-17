from MainDick.Point import Point

class Vector:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        

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