from MainDick.ForceController import ForceController
from MainDick.Vector import Vector
from math import radians, cos, sin


class Spacecraft:
    def __init__(self, name, power, mass, position, image, direction=0, radius=35):

        self.name = name
        self.power = power
        self.mass = mass
        self.position = position
        self.image = image
        self.direction = direction
        self.radius = radius

    def fly(self, planets, direction):

        gravity_vector = ForceController().calculate_gravity_vector(planets, self)
        thrust_vector = Vector(0, 0)
        direction_change = 0

        if direction is not None:
            if 'w' == direction.char:
                direction_change += 5

            if 'a' == direction.char:
                direction_change -= 5

            if 's' == direction.char:
                thrust_vector = thrust_vector.sum(self.vector_from_len_and_angle(self.power, self.direction))

            if 'd' == direction.char:
                thrust_vector = thrust_vector.sum(self.vector_from_len_and_angle(self.power / 2, self.direction + 180))

        movement_vector = gravity_vector.sum(thrust_vector)
        self.direction += direction_change

        return movement_vector.to_list()[0], movement_vector.to_list()[1], self.direction

    def vector_from_len_and_angle(self, len, angle):

        return Vector(len * sin(radians(angle)), len * cos(radians(angle)))
