import math


class FrontScanner:

    def will_collide(self, ship, planet_candidates, max_width, max_height):
        a = math.tan(math.pi + math.radians(ship.direction))
        b = math.fabs(max_height-ship.position.y)- a * math.fabs(max_width-ship.position.x)
        print(a, b, ship.direction, ship.position.x, ship.position.y)
        for planet in planet_candidates:
            prox = abs(a * math.fabs(max_width-planet.coordinates.x) - math.fabs(max_height-planet.coordinates.y) + b) / math.sqrt((a ** 2) + 1)
            if prox <= (planet.radius + ship.radius) and self.plausible_coords(ship.direction, ship.position, planet.coordinates):
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






