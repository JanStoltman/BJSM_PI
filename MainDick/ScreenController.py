import tkinter
from PIL import Image, ImageTk
from MainDick.SpaceObjects.Planet import Planet
from MainDick.SpaceObjects.Spacecraft import Spacecraft


class ScreenController:
    def __init__(self, background):
        self.screen = tkinter.Tk()
        self.screen.update()
        self.screen.geometry("{0}x{1}+0+0".format(
            self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()))
        self.width = self.screen.winfo_screenwidth()
        self.height = self.screen.winfo_screenheight()

        self.background = background
        self.spacecraft_bitmap = None
        self.planets = None
        self.filename = None
        self.background_filename = None
        self.planet_filenames = []

        self.canvas = tkinter.Canvas(self.screen, bg="black", height=self.height, width=self.width)

        self.width = self.screen.winfo_screenwidth() - 75
        self.height = self.screen.winfo_screenheight() - 50

    def show_screen(self):
        self.screen.mainloop()

    def add_planet(self, planets):
        for p in planets:
            x = p.coordinates.x
            y = p.coordinates.y
            self.planet_filenames.append(tkinter.PhotoImage(file=p.image))
            self.planet_filenames[-1] = self.planet_filenames[-1].subsample(int(125 / p.radius), int(125 / p.radius))
            self.canvas.create_image((x, y), image=self.planet_filenames[-1])

    def add_spacecraft(self, spacecraft):
        image = Image.open(spacecraft.image)
        self.filename = ImageTk.PhotoImage(image.rotate(spacecraft.direction))
        self.spacecraft_bitmap = self.canvas.create_image((spacecraft.position.x, spacecraft.position.y),
                                                          image=self.filename)

    def move_spacecraft(self, updated_spacecraft):
        self.canvas.delete(self.spacecraft_bitmap)
        image = Image.open(updated_spacecraft.image)
        self.filename = ImageTk.PhotoImage(image.rotate(updated_spacecraft.direction))
        self.spacecraft_bitmap = self.canvas.create_image(
            (updated_spacecraft.position.x, updated_spacecraft.position.y),
            image=self.filename)

    def pack_canvas(self, _planets, _spacecraft):
        self.canvas.pack()
        self.set_background_image()
        self.add_planet(planets=_planets)
        self.add_spacecraft(spacecraft=_spacecraft)

    def set_background_image(self):
        self.background_filename = tkinter.PhotoImage(file=self.background)
        self.canvas.create_image(0, 0, image=self.background_filename, anchor="nw")
