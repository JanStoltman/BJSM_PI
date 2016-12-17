from MainDick.Point import Point
import math

class RadarController:

    def scan_for_planets(self, planets, radar_radius, ship_position, space_width, space_height):
        search_square = self.convert_to_square(2 * radar_radius, ship_position.x, ship_position.y, space_width, space_height)
        planets_to_scan_for = self.planets_in_square(planets, search_square)
        planets_in_sight = self.planets_detected(planets_to_scan_for, radar_radius, ship_position)

        return planets_in_sight


    def convert_to_square(self, half_side, center_x, center_y, max_x, max_y):
        left_lower_x = center_x - half_side if center_x - half_side >= 0 else 0
        left_lower_y = center_y - half_side if center_y - half_side >= 0 else 0
        right_upper_x = center_x + half_side if center_x + half_side <= max_x else max_x
        right_upper_y = center_y + half_side if center_y + half_side <= max_y else max_y

        return (left_lower_x, left_lower_y), (right_upper_x, right_upper_y)


    def planets_in_square(self, planets, square):
        list_of_planets_in_square = []
        for planet in planets:
            if planet.coordinates.x >= square[0][0] and planet.coordinates.x <= square[1][0] and planet.coordinates.y >= square[0][1] and planet.coordinates.y <= square[1][1]:
                list_of_planets_in_square.append(planet)

        return list_of_planets_in_square


    def planets_detected(self, possible_planets, radius, ship_coords):
        detected_planets_list = []
        for planet in possible_planets:
            if self.close_enough(planet.coordinates, ship_coords, planet.radius + radius):
                detected_planets_list.append(planet)

        return detected_planets_list


    def close_enough(self, planet_coords, ship_coords, max_distance):
        return  planet_coords.proximity(ship_coords) < max_distance

