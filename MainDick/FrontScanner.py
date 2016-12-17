import math


class FrontScanner:
    def will_collide(self, ship, planet_candidates, max_width, max_height):
        for planet in planet_candidates:
            if planet.mass > 0 and math.hypot(planet.coordinates.x - ship.position.x,
                          planet.coordinates.y - ship.position.y) <= planet.radius + (ship.radius * (math.fabs(ship.speed) / 10 + 1)):
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
