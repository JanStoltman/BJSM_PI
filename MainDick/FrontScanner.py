import math


class FrontScanner:

    def will_collide(self, ship, planet_candidates):
        a = math.tan(math.radians(ship.direction) + math.pi / 2)
        b = ship.position.y - a * ship.position.x
        for planet in planet_candidates:
            prox = abs(a * planet.coordinates.x - planet.coordinates.y + b) / math.sqrt((a ** 2) + 1)
            if prox <= planet.radius and self.plausible_coords(ship.direction, ship.position, planet.coordinates):
                return True
        return False

    def plausible_coords(self, dir, ship_pos, planet_coords):
        if dir < 90:
            return planet_coords.x > ship_pos.x and planet_coords.y > planet_coords.y
        elif dir >= 90 and dir < 180:
            return planet_coords.x <= ship_pos.x and planet_coords.y > planet_coords.y
        elif dir >= 180 and dir < 270:
            return planet_coords.x <= ship_pos.x and planet_coords.y <= planet_coords.y
        else:
            return planet_coords.x > ship_pos.x and planet_coords.y <= planet_coords.y






