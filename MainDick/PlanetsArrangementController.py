from MainDick.SpaceObjects.Planet import Planet
import random

class PlanetsArrangementController:

    def arrange_planets(self, number_of_planets, colors_list, minimal_distance, min_mass, max_mass, min_radius, max_radius,
                        max_width, max_height, margin):

        if max_width < 2 * margin or max_height < 2 * margin:
            raise ValueError('Too big margin value')

        list_of_planets = []

        if number_of_planets >= 1:
            first_planet = Planet('planet0',
                                  random.choice(colors_list),
                                  random.randint(min_mass, max_mass),
                                  random.randint(min_radius, max_radius),
                                  (random.randint(margin, max_width - margin), random.randint(margin, max_height - margin)))

            list_of_planets.append(first_planet)

        for i in range(1, number_of_planets):
            next_planet = Planet('planet' + str(i),
                                  random.choice(colors_list),
                                  random.randint(min_mass, max_mass),
                                  random.randint(min_radius, max_radius),
                                  (random.randint(margin, max_width - margin), random.randint(margin, max_height - margin)))

            list_of_planets.append(next_planet)

        return list_of_planets

