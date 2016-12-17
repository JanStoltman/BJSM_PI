class GameController:

    def flight(self, planets, ship, max_x, max_y):



        ship.position.x = ship.position.x + 10
        ship.position.y = ship.position.y + 20
        ship.direction = (ship.direction + 10) % 360

        return ship


    def is_dead(self, planets, ship):

        return self.is_out_of_space(ship.position) or self.crashed(planets, ship.position)


    def reached_destination(self, ship_position, destination):

        return ship_position.proximity(destination.coordinates) <= destination.radius


    def is_out_of_space(self, ship_position, max_x, max_y):

        return not ship_position.x in range(0, max_x) and ship_position.y in range(0, max_y)


    def crashed(self, planets, ship_position):

        for planet in planets:
            if self.reached_destination(ship_position, planet):
                return True
        return False



