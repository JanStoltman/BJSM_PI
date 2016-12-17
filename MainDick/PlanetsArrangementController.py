from MainDick.SpaceObjects.Planet import Planet
from MainDick.Point import Point
from MainDick.ImageLoader import get_space_station_image
import random


class PlanetsArrangementController:
    def arrange_planets(self, number_of_planets, minimal_distance,
                        files_list,
                        min_mass, max_mass,
                        min_radius, max_radius,
                        max_width, max_height,
                        margin):

        space_station_radius = 50

        if max_width < 2 * margin + space_station_radius or  max_height < 2 * margin + space_station_radius:
            raise ValueError('Not enough space')


        list_of_planets = []
        list_of_coords = []

        space_station = Planet('space station', 0, space_station_radius,
                                Point(random.randint(margin + space_station_radius,
                                                  int(max_width / 3) - space_station_radius),
                                random.randint(margin + space_station_radius,
                                                  int(max_height / 3) - space_station_radius)),
                                image=get_space_station_image())

        list_of_planets.append(space_station)

        for i in range(number_of_planets):
            list_of_coords.append(list_of_planets[-1].coordinates)

            next_planet_radius = random.randint(min_radius, max_radius)

            next_planet_coords = Point(random.randint(margin + next_planet_radius, max_width - margin - next_planet_radius-400),
                                  random.randint(margin + next_planet_radius, max_height - margin - next_planet_radius-400))
            loop_guardian = 0

            while not self.acceptable_coordinates(list_of_coords, next_planet_coords, minimal_distance):
                next_planet_coords = Point(
                    random.randint(margin + next_planet_radius, max_width - margin - next_planet_radius - 400),
                    random.randint(margin + next_planet_radius, max_height - margin - next_planet_radius - 400))
                loop_guardian += 1
                if loop_guardian >= 100:
                    return list_of_planets

            next_planet = Planet('planet' + str(i),
                                 random.randint(min_mass, max_mass),
                                 next_planet_radius,
                                 next_planet_coords,
                                 image=files_list[i%10])

            list_of_planets.append(next_planet)

        return list_of_planets

    def acceptable_coordinates(self, list_of_coords, curr_planet_coords, min_distance):

        for prev_coords in list_of_coords:
            if curr_planet_coords.proximity(prev_coords) < min_distance:
                return False

        return True
