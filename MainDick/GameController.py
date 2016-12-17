class GameController:
    @staticmethod
    def flight(planets, ship, max_x, max_y):

        x = -10
        y = -20
        z = (ship.direction + 10) % 360

        return (x, y, z)

    def is_dead(self, planets, ship):

        return self.is_out_of_space(ship.position) or self.crashed(planets, ship.position)

    @staticmethod
    def reached_destination(ship_position, destination):

        return ship_position.proximity(destination.coordinates) <= destination.radius

    @staticmethod
    def is_out_of_space(ship_position, max_x, max_y):

        return not ship_position.x in range(0, max_x) and ship_position.y in range(0, max_y)

    def crashed(self, planets, ship_position):

        for planet in planets:
            if self.reached_destination(ship_position, planet):
                return True
        return False
