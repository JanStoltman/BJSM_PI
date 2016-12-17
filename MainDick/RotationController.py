from math import atan2, degrees, pi


def get_rotation(spacecraft, base_position):
    dx = spacecraft.position.x -base_position[0]
    dy = spacecraft.position.y - base_position[1]
    return spacecraft.direction - degrees(atan2(float(dx), float(dy)))
