from MainDick.ForceController import ForceController
from MainDick.RadarController import RadarController
from MainDick.FrontScanner import FrontScanner
from MainDick.RotationController import RotationController
from MainDick.Vector import Vector
import math


class FlightController:

    def acceleration_control(self, ship, planets, radar_radius, max_width, max_height, tick):

        radarController = RadarController()

        movement_vector = ForceController().calculate_movement_vector(planets, ship)
        planets_on_radar = radarController.scan_for_planets(planets, radar_radius, ship.position.x,
                                                              ship.position.y, max_width, max_height)

        ship.position.x += movement_vector.X
        ship.position.y += movement_vector.Y
        temp_dir = RotationController().get_rotation(ship, planets[0].coordinates)

        if FrontScanner().will_collide(ship, planets_on_radar):
            direction, turn = self.rotation_control(ship, planets[0].position, planets_on_radar)
            if turn is None:
                return movement_vector.X, movement_vector.Y, ship.speed, 0, ship.fuel

            if ship.fuel >= turn:
                return movement_vector.X, movement_vector.Y, ship.speed, direction, ship.fuel - turn

            else:
                return movement_vector.X, movement_vector.Y, ship.speed, 0, ship.fuel

        check = 0

        while radarController.scan_for_planets(planets, int(radar_radius / (5 + 2 * check)), ship.position.x,
                                             ship.position.y, max_width, max_height) and ship.fuel - check >= 0:
            check += 1

        movement_x, movement_y, speed = self.accelerate(check, ship, tick)

        return movement_vector.X + movement_x, movement_vector.Y + movement_y, speed, temp_dir, ship.fuel - check

    def rotation_control(self, ship, base_position, planets_on_radar):

        ship2 = ship

        for turn, angle in enumerate(range(15, 61, 15)):
            begin = 1 if RotationController().get_rotation(ship, base_position) > ship.direction else -1

            direction = angle * begin
            ship2.direction = ship.direction + direction
            if not FrontScanner().will_collide(ship2, planets_on_radar):
                return direction, turn

            direction = angle * begin * -1
            ship2.direction = ship.direction + direction
            if not FrontScanner().will_collide(ship2, planets_on_radar):
                return direction, turn

        return direction, None


    def accelerate(self, unit, ship, tick):

        acceleration_vector = Vector(unit * math.sin(ship.direction), unit * math.cos(ship.direction))
        scalar = int(tick ** 2 / 2) + 1
        movement_vector = acceleration_vector.multiply(scalar)

        return movement_vector.X, movement_vector.Y, ship.speed + unit