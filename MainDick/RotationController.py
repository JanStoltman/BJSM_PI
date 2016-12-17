from math import atan2, degrees, pi


def get_rotation(spacecraft, base_position):
    dx = spacecraft.position.x - base_position.x
    dy = spacecraft.position.y - base_position.y
    return degrees(atan2(float(dx), float(dy)))
