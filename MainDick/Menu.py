from ipywidgets import interact, fixed
import ipywidgets as widgets
from MainDick.ScreenController import ScreenController
from MainDick.SpaceObjects.Spacecraft import Spacecraft
from MainDick.PlanetsArrangementController import PlanetsArrangementController
from MainDick.Point import Point
from MainDick.SpaceObjects.Planet import Planet

import MainDick.ImageLoader as ImL

def run_sim(name, power, fuel, mass, position, image, ready, speed = 20, direction = 0,radius = 35):
    statek = Spacecraft(name,power,fuel,mass,position,image,speed,direction,radius)
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
    if ready:
        screenController.pack_canvas(planets, statek)
        screenController.show_screen()


interact(run_sim, name='Name', power=10.0, fuel=10.0, mass=10.0, position=(0,0),
         image=fixed(ImL.get_spacecraft_image()), speed=20.0, direction=0, radius=fixed(35), ready=False)
