import MainDick.Vectors.vectors as vectors

def proximity(ship, planet):
    return ((ship.coordinates[0]-planet.coordinates[0])**2+(ship.coordinates[1]-planet.coordinates[1])**2)**(1/2)
def gravity(ship, planet):
    return 6.67*planet.mass()*ship.mass()/proximity(ship.coords(), planet)**2
def grav_vector(ship, planet):
     v = vectors.Vector.from_points(ship.coordinates,planet.coordinates)
     v.multiply(gravity(ship, planet)/v.magnitude())
     return v
def net_move(gravs, thrust, tick=1):
    net = vectors.Vector(0,0,0)
    for v in gravs:
        net.sum(v.multiply(tick**2/2))
    return net.sum(thrust.multiply(tick))

