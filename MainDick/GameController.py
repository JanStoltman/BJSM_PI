class GameController:
    @staticmethod
    def flight(planets, ship, max_x, max_y):

        x = -10
        y = -20
        z = (ship.direction + 10) % 360

        return (x, y, z)

    def is_dead(self, planets, ship, max_x, max_y):

        return self.is_out_of_space(ship.position, max_x=max_x, max_y=max_y) or self.crashed(planets, ship)

    @staticmethod
    def reached_destination(spacecraft, destination):

        return spacecraft.position.proximity(destination.coordinates) - spacecraft.radius <= destination.radius

    @staticmethod
    def is_out_of_space(ship_position, max_x, max_y):

        return not ship_position.x in range(0, max_x) and ship_position.y in range(0, max_y)

    def crashed(self, planets, spacecraft):

        for planet in planets:
            if self.reached_destination(spacecraft, planet):
                return True
        return False
