from MainDick.ImageLoader import get_spacecraft_image
from MainDick.SpaceObjects.Spacecraft import Spacecraft
from MainDick.SpaceObjects.Planet import Planet
from MainDick.Point import Point
from MainDick.Vector import Vector

def gravity(ship, planet):
    return 6.67*planet.mass*ship.mass/ship.position.proximity(planet.coordinates)**2


def from_points(point1, point2):
    return Vector(point2.x - point1.x, point2.y - point1.y)

def grav_vector(ship, planet):
    v = from_points(ship.position, planet.coordinates)
    v = v.multiply(gravity(ship, planet)/v.magnitude())
    return v


def net_move(gravs):
    net = Vector(0, 0)
    for v in gravs:
        print(v.to_list())
        print(net.to_list())
        net = net.sum(v)
        print(net.to_list())
    return net

"""
def movement(net_r, ship):
    ship.position.x = ship.position.x+net_r.X
    ship.position.y = ship.position.y+net_r.Y
"""

statek = Spacecraft('stateczek', 10, 10, 10, Point(1, 1), get_spacecraft_image())
planeta = Planet('Jebudu', 10, 10, Point(5, 4), get_spacecraft_image())
vec = grav_vector(statek,planeta)
print(net_move([vec]))
