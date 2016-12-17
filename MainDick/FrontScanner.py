from MainDick.Point import Point
from MainDick.SpaceObjects.Spacecraft import Spacecraft
from math import tan, pi
class FrontScanner:

    def will_collide(self, ship, planet_candidates):
        a = tan((ship.direction*pi/180)+pi/2)
        b = ship.position.y - a*ship.position.x
        for planet in planet_candidates:
            prox = abs(a*planet.coordinates.x-planet.coordinates.y+b)/(((a**2)+1)**(1/2))
            if prox <= planet.radius and planet.mass > 0:
                return True
        return False






