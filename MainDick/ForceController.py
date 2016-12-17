from MainDick.Vector import Vector
import math

class ForceController:

    def gravity(self, ship, planet):
        G = 6.67
        return G * planet.mass * ship.mass / ship.position.proximity(planet.coordinates) ** 2


    def from_points(self, point1, point2):
        return Vector(point2.x - point1.x, point2.y - point1.y)


    def gravity_vector(self, ship, planet):
        v = self.from_points(ship.position, planet.coordinates)
        v = v.multiply(self.gravity(ship, planet) / v.magnitude())
        return v


    def net_gravity(self, gravity_vectors):
        net = Vector(0, 0)
        for v in gravity_vectors:
            net = net.sum(v)
        return net


    def calculate_movement_vector(self, planets, ship, tick = 1):
        gravity_vectors_list = []
        for planet in planets:
            gravity_vectors_list.append(self.gravity_vector(ship, planet))

        gravity = self.net_gravity(gravity_vectors_list).multiply(tick ** 2 / 2 * ship.mass)
        gravity = Vector(int(gravity.X), int(gravity.Y))

        movement = Vector(int(ship.speed * tick * math.sin(ship.direction)), int(ship.speed * tick * math.cos(ship.direction)))

        return gravity.sum(movement)