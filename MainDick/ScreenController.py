import tkinter
from MainDick.SpaceObjects.Planet import Planet
from MainDick.SpaceObjects.Spacecraft import Spacecraft


class ScreenController:
    def __init__(self):
        self.screen = tkinter.Tk()
        self.screen.update()
        self.screen.geometry("{0}x{1}+0+0".format(
            self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()))
        self.width = self.screen.winfo_screenwidth()
        self.height = self.screen.winfo_screenheight()
        self.spacecraft_bitmap = None
        self.planets = None
        self.filename = None
        self.canvas = tkinter.Canvas(self.screen, bg="black", height=self.height, width=self.width)

    def show_screen(self):
        self.screen.mainloop()

    def add_planet(self, planets):
        for p in planets:
            x = p.coordinates[0]
            y = p.coordinates[1]
            self.canvas.create_oval(x - p.radius, y - p.radius,
                                    x + p.radius, y + p.radius,
                                    fill=p.color)

    def add_spacecraft(self, spacecraft):
        self.filename = tkinter.PhotoImage(file=spacecraft.image)
        self.spacecraft_bitmap = self.canvas.create_image((spacecraft.position_x, spacecraft.position_y),
                                                          image=self.filename)

    def pack_canvas(self, _planets, _spacecraft):
        self.canvas.pack()
        self.add_planet(planets=_planets)
        self.add_spacecraft(spacecraft=_spacecraft)

