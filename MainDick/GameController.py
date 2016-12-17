from MainDick.Point import Point

class GameController:

    def flight(self, planets, ship, max_x, max_y):



        ship.position_x = ship.position_x + 10
        ship.position_y = ship.position_y + 20
        ship.direction = (ship.direction + 10) % 360


    def is_dead(self, planets, ship):

        return is_out_of_space(planets, ship) or crashed(planets, ship)


    def reached_destination(self, ship, destination):

        return



