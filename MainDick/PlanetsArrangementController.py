from MainDick.SpaceObjects.Planet import Planet
import random
import math


class PlanetsArrangementController:
    def arrange_planets(self, number_of_planets, minimal_distance,
                        files_list,
                        min_mass, max_mass,
                        min_radius, max_radius,
                        max_width, max_height,
                        margin):

        if max_width < 2 * margin or max_height < 2 * margin:
            raise ValueError('Too big margin value')

        list_of_planets = []
        list_of_coords = []

        if number_of_planets >= 1:
            first_planet_radius = random.randint(min_radius, max_radius)
            first_planet = Planet('planet0',
                                  random.randint(min_mass, max_mass),
                                  first_planet_radius,
                                  (random.randint(margin + first_planet_radius,
                                                  max_width - margin - first_planet_radius),
                                   random.randint(margin + first_planet_radius,
                                                  max_height - margin - first_planet_radius)),
                                  image=random.choice(files_list))

            list_of_planets.append(first_planet)

        for i in range(1, number_of_planets):
            list_of_coords.append(list_of_planets[-1].coordinates)

            next_planet_radius = random.randint(min_radius, max_radius)

            next_planet_coords = (random.randint(margin + next_planet_radius, max_width - margin - next_planet_radius),
                                  random.randint(margin + next_planet_radius, max_height - margin - next_planet_radius))
            loop_guardian = 0

            while not self.acceptable_coordinates(list_of_coords, next_planet_coords, minimal_distance):
                next_planet_coords = (
                    random.randint(margin + next_planet_radius, max_width - margin - next_planet_radius),
                    random.randint(margin + next_planet_radius, max_height - margin - next_planet_radius))
                loop_guardian += 1
                if loop_guardian >= 100:
                    return list_of_planets

            next_planet = Planet('planet' + str(i),
                                 random.randint(min_mass, max_mass),
                                 next_planet_radius,
                                 (next_planet_coords[0], next_planet_coords[1]),
                                 image=random.choice(files_list))

            list_of_planets.append(next_planet)

        return list_of_planets

    def acceptable_coordinates(self, list_of_coords, curr_planet_coords, min_distance):

        curr_x, curr_y = curr_planet_coords

        for prev_x, prev_y in list_of_coords:
            if math.sqrt((curr_x - prev_x) ** 2 + (curr_y - prev_y) ** 2) < min_distance:
                return False

        return True
