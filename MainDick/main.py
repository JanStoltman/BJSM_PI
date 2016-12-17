from MainDick.ScreenController import ScreenController
from MainDick.SpaceObjects.Spacecraft import Spacecraft
from MainDick.PlanetsArrangementController import PlanetsArrangementController
from MainDick.Point import Point
from MainDick.SpaceObjects.Planet import Planet

import MainDick.ImageLoader as ImL

screenController = ScreenController(background=ImL.get_background_image())
planets = PlanetsArrangementController().arrange_planets(number_of_planets=7,
                                                         minimal_distance=300,
                                                         min_mass=10,
                                                         min_radius=30,
                                                         max_mass=100,
                                                         max_radius=50,
                                                         max_height=screenController.height,
                                                         max_width=screenController.width,
                                                         margin=10,
                                                         files_list=ImL.get_planet_images())

craft = Spacecraft(fuel=100, power=10, mass=10,
                   position=Point(screenController.width, screenController.height),
                   image=ImL.get_destroyer_image(), name="Dupa", direction=180, radius = 35)

screenController.pack_canvas(planets, craft)
screenController.show_screen()
