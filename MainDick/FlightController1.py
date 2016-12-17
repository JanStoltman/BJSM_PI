from MainDick.ForceController import ForceController
from MainDick.RadarController import RadarController
from MainDick.FrontScanner import FrontScanner
from MainDick.Vector import Vector
import math

class FlightController1:

    def acceleration_control(self, ship, planets, speed, radar_radius, max_width, max_height, tick = 1):

        radarController = RadarController()

        movement_vector = ForceController().calculate_movement_vector(planets, ship, speed)
        planets_on_radar = radarController.scan_for_planets(planets, radar_radius, ship.position.x,
                                                              ship.position.y, max_width, max_height)

        ship.position.x += movement_vector.X
        ship.position.y += movement_vector.Y

        if FrontScanner().will_collide(ship, planets_on_radar):
            # funkcja z FC2

        check = 0

        while radarController.scan_for_planets(planets, radar_radius / (5 + 2 * check), ship.position.x,
                                             ship.position.y, max_width, max_height) and ship.fuel - check >= 0:
            check += 1

        ship.position.x, ship.position.y, ship.speed = self.accelerate(check, ship, tick)
        ship.fuel -= check


    def accelerate(self, unit, ship, tick):

        acceleration_vector = Vector(unit / math.sin(ship.direction), unit / math.cos(ship.direction))
        movement_vector = acceleration_vector.multiply(tick ** 2 / 2)

        return ship.position.x + movement_vector.X, ship.position.y + movement_vector.Y, ship.speed + unit