from MainDick.ScreenController import ScreenController
from MainDick.SpaceObjects.Spacecraft import Spacecraft
from MainDick.PlanetsArrangementController import PlanetsArrangementController

screenController = ScreenController()
planets = PlanetsArrangementController().arrange_planets(number_of_planets=3, colors_list=["#32cd32", "#ffd700", "#bc8f8f"],
                                                         minimal_distance=10,
                                                         min_mass=10,
                                                         min_radius=5,
                                                         max_mass=100,
                                                         max_radius=20,
                                                         max_height=screenController.height,
                                                         max_width=screenController.width,
                                                         margin=10)
craft = Spacecraft(fuel=100, power=10, mass=10,
                   position_x=screenController.width, position_y=screenController.height,
                   image="Spacecraft.png",name="Dupa")

screenController.pack_canvas(planets, craft)
screenController.show_screen()
