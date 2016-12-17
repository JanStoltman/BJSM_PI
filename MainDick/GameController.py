from MainDick.FlightController import FlightController

class GameController:
    @staticmethod
    def flight(planets, ship, max_x, max_y, tick = 1):

        flightController = FlightController()

        return flightController.acceleration_control(ship, planets, 400, max_x, max_y, tick)

    def is_dead(self, planets, ship, max_x, max_y):

        return self.is_out_of_space(ship.position, max_x=max_x, max_y=max_y) or self.crashed(planets, ship)

    @staticmethod
    def reached_destination(spacecraft, destination):

        return spacecraft.position.proximity(destination.coordinates) - spacecraft.radius <= destination.radius

    @staticmethod
    def is_out_of_space(ship_position, max_x, max_y):

        return  ship_position.x not in range(0, max_x) or ship_position.y not in range(0, max_y)

    def crashed(self, planets, spacecraft):

        for planet in planets:
            if self.reached_destination(spacecraft, planet) and planet.mass > 0:
                return True
        return False

    def has_won(self, spacecraft):
        return self.reached_destination(spacecraft, spacecraft.base_station)
