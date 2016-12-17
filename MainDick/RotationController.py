from math import atan2, degrees, pi

class RotationController:


    def get_rotation(self, spacecraft, base_position):
        dx = spacecraft.position.x - base_position.x
        dy = spacecraft.position.y - base_position.y
        return degrees(atan2(float(dx), float(dy)))
