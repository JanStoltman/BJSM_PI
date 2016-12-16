

class RadarController:

    def scan_for_planets(self, planets, radar_radius, ship_position, space_width, space_height):
        search_square = self.convert_to_square(radar_radius, ship_position, space_width, space_height)


    def convert_to_square(self, half_side, center, max_x, max_y):
        left_lower_x = center[0] - side if center[0] - side >= 0 else 0