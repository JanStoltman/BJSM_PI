import math
from MainDick.Vector import Vector


class FrontScanner:
    def will_collide(self, ship, planet_candidates, max_width, max_height):
        for planet in planet_candidates:
            connecting_vector = self.from_points(ship.position, planet.coordinates)
            tan = connecting_vector.X / connecting_vector.Y if connecting_vector.Y != 0 else 100000

            print(connecting_vector.to_list(), tan)

            if tan <= math.tan(math.radians(ship.direction)) + 0.5 and tan >= math.tan(math.radians(ship.direction)) - 0.5:

                return True

        return False


    def plausible_coords(self, dir, ship_pos, planet_coords):
        if dir < 90:
            return planet_coords.x >= ship_pos.x and planet_coords.y < ship_pos.y
        elif dir >= 90 and dir < 180:
            return planet_coords.x >= ship_pos.x and planet_coords.y >= ship_pos.y
        elif dir >= 180 and dir < 270:
            return planet_coords.x < ship_pos.x and planet_coords.y >= ship_pos.y
        else:
            return planet_coords.x < ship_pos.x and planet_coords.y < ship_pos.y


    def from_points(self, point1, point2):
        return Vector(point2.x - point1.x, point2.y - point1.y)
