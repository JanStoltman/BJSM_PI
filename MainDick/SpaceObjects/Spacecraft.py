from MainDick.ForceController import ForceController
from MainDick.Vector import Vector
from math import radians, cos, sin

class Spacecraft:


    def __init__(self, name, power, fuel, mass, position, image, direction = 0,radius = 35):

        self.name = name
        self.power = power
        self.fuel = fuel
        self.mass = mass
        self.position = position
        self.image = image
        self.direction = direction
        self.radius = radius


    def fly(self, planets, direction):

        gravity_vector = ForceController().calculate_gravity_vector(planets, self)

        if direction == 'fd':
            thrust_vector = self.vector_from_len_and_angle(self.power, self.direction)
            movement_vector = gravity_vector.sum(thrust_vector)

        elif direction == 'lt':
            thrust_vector = self.vector_from_len_and_angle(self.power, self.direction + 90)
            movement_vector = gravity_vector.sum(thrust_vector)

        elif direction == 'rt':
            thrust_vector = self.vector_from_len_and_angle(self.power, self.direction - 90)
            movement_vector = gravity_vector.sum(thrust_vector)

        else:
            movement_vector = gravity_vector

        self.position.x += movement_vector.X
        self.position.y += movement_vector.Y

        return movement_vector


    def vector_from_len_and_angle(self, len, angle):

        return Vector(len * sin(radians(angle)), len * cos(radians(angle)))




