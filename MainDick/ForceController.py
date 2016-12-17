from MainDick.ImageLoader import get_spacecraft_image
from MainDick.SpaceObjects.Spacecraft import Spacecraft
from MainDick.SpaceObjects.Planet import Planet
from MainDick.Point import Point
from MainDick.Vector import Vector

class ForceController:

    def gravity(self, ship, planet):
        G = 6.67 * 10 ** -11
        return G * planet.mass * ship.mass / ship.position.proximity(planet.coordinates) ** 2


    def from_points(self, point1, point2):
        return Vector(point2.x - point1.x, point2.y - point1.y)


    def grav_vector(self, ship, planet):
        v = self.from_points(ship.position, planet.coordinates)
        v = v.multiply(self.gravity(ship, planet) / v.magnitude())
        return v


    def net_gravity(self, gravs):
        net = Vector(0, 0)
        for v in gravs:
            net = net.sum(v)
        return net


    def calculate_movement_vector(self, planets, ship):



