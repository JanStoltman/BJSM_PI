from MainDick.ForceController import ForceController
from MainDick.Vector import Vector
from math import radians, cos, sin

class Spacecraft:


    def __init__(self, name, power, mass, position, image, direction = 0,radius = 35):

        self.name = name
        self.power = power
        self.mass = mass
        self.position = position
        self.image = image
        self.direction = direction
        self.radius = radius


    def fly(self, planets, directions):

        gravity_vector = ForceController().calculate_gravity_vector(planets, self)
        thrust_vector = (0, 0)

        if 'lt' in directions:
            self.direction += 5

        if 'rt' in directions:
            self.direction -= 5

        if 'fd' in directions:
            thrust_vector = thrust_vector.sum(self.vector_from_len_and_angle(self.power, self.direction))

        if 'bk' in directions:
            thrust_vector = thrust_vector.sum(self.vector_from_len_and_angle(self.power / 2, self.direction + 180))

        movement_vector = gravity_vector.sum(thrust_vector)

        self.position.x += movement_vector.X
        self.position.y += movement_vector.Y

        return movement_vector.to_list()


    def vector_from_len_and_angle(self, len, angle):

        return Vector(len * sin(radians(angle)), len * cos(radians(angle)))




