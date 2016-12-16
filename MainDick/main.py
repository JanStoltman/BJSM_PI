from MainDick.ScreenController import ScreenController
from MainDick.SpaceObjects.Spacecraft import Spacecraft
from MainDick.PlanetsArrangementController import PlanetsArrangementController

import MainDick.ImageLoader as ImL

screenController = ScreenController()
planets = PlanetsArrangementController().arrange_planets(number_of_planets=3,
                                                         minimal_distance=300,
                                                         min_mass=10,
                                                         min_radius=5,
                                                         max_mass=100,
                                                         max_radius=125,
                                                         max_height=screenController.height,
                                                         max_width=screenController.width,
                                                         margin=10,
                                                         files_list=ImL.get_planet_images())
craft = Spacecraft(fuel=100, power=10, mass=10,
                   position_x=screenController.width, position_y=screenController.height,
                   image=ImL.get_spacecraft_image(), name="Dupa")

screenController.pack_canvas(planets, craft)
screenController.show_screen()
