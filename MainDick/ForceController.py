import MainDick.Vectors.vectors as vectors
from MainDick.ImageLoader import get_spacecraft_image
from MainDick.SpaceObjects.Spacecraft import Spacecraft
from MainDick.SpaceObjects.Planet import Planet
from MainDick.Point import Point

def gravity(ship, planet):
    return 6.67*planet.mass*ship.mass/ship.position.proximity(planet.coordinates)**2
def grav_vector(ship, planet):
    ship_coordinates = vectors.Point(ship.position.x, ship.position.y, ship.position.z)
    planet_coordinates = vectors.Point(planet.coordinates.x, planet.coordinates.y, planet.coordinates.z)
    v = vectors.Vector.from_points(ship_coordinates, planet_coordinates)
    v = v.multiply(gravity(ship, planet)/v.magnitude())
    return v
def net_move(gravs):
    net = vectors.Vector(0,0,0)
    for v in gravs:
        print(v.vector)
        print(net.vector)
        net = net.sum(v)
        print(net.vector)
    return net
def movement(net_r, ship):
    ship.position.x = ship.position.x+net_r.vector[0]
    ship.position.y = ship.position.y+net_r.vector[1]

statek = Spacecraft('stateczek', 10, 10, 10, Point(1, 1), get_spacecraft_image())
planeta = Planet('Jebudu', 10, 10, Point(5,4), get_spacecraft_image())
vec = grav_vector(statek,planeta)
print(net_move([vec]))
