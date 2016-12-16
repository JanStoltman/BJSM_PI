from MainDick.SpaceObjects.Planet import Planet
import random

class PlanetsArrangementController:

    def arrange_planets(self, number, colors, minimal_distance, min_mass, max_mass, min_radius, max_radius,
                        max_width, max_height, margin):

        if max_width < margin or max_height < margin:
            raise ValueError('Too big margin value')

        list_of_planets = []

        if number >= 1:
            first_planet = Planet('planet0',
                                  random.choice(colors),
                                  random.randint(min_mass, max_mass),
                                  random.randint(min_radius, max_radius),
                                  (random.randint(margin, max_width - margin), random.randint(margin, max_height - margin)))

            list_of_planets.append(first_planet)

        for _ in range(1, number):

