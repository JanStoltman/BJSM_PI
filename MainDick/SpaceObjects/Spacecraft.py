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
        direction_change = 0

        if 'W' in directions:
            direction_change += 5

        if 'A' in directions:
            direction_change -= 5

        if 'S' in directions:
            thrust_vector = thrust_vector.sum(self.vector_from_len_and_angle(self.power, self.direction))

        if 'D' in directions:
            thrust_vector = thrust_vector.sum(self.vector_from_len_and_angle(self.power / 2, self.direction + 180))

        movement_vector = gravity_vector.sum(thrust_vector)

        self.position.x += movement_vector.X
        self.position.y += movement_vector.Y
        self.direction += direction_change

        return movement_vector.to_list()[0], movement_vector.to_list()[1], direction_change


    def vector_from_len_and_angle(self, len, angle):

        return Vector(len * sin(radians(angle)), len * cos(radians(angle)))




