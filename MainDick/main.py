from MainDick.ScreenController import ScreenController
from MainDick.SpaceObjects.Spacecraft import Spacecraft
from MainDick.PlanetsArrangementController import PlanetsArrangementController
from MainDick.Point import Point

import MainDick.ImageLoader as ImL

screenController = ScreenController(background=ImL.get_background_image())
planets = PlanetsArrangementController().arrange_planets(number_of_planets=8,
                                                         minimal_distance=300,
                                                         min_mass=1,
                                                         min_radius=30,
                                                         max_mass=2,
                                                         max_radius=50,
                                                         max_height=screenController.height,
                                                         max_width=screenController.width,
                                                         margin=10,
                                                         files_list=ImL.get_planet_images())

craft = Spacecraft(fuel=100, power=20, mass=10,
                   position=Point(screenController.width - 50, screenController.height - 50),
                   image=ImL.get_destroyer_image(),
                   base_station=base_station, name="Dupa", direction=180, radius=35, speed=-10)

screenController.pack_canvas(planets, craft)
planets = planets[1:]
screenController.show_screen()
