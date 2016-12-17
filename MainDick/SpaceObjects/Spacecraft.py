from MainDick.ForceController import ForceController
from MainDick.Vector import Vector

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
            thrust_vector = Vector().from_len_and_angle(len, angle)
        elif direction == 'lt':

        elif direction == 'rt':

        else:
            raise ValueError('Wrong direction')




