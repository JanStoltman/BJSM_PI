import tkinter
from tkinter import messagebox

from PIL import Image, ImageTk

import MainDick.ImageLoader as ImL
from MainDick.GameController import GameController


class ScreenController:
    def __init__(self, background):
        self.screen = tkinter.Tk()
        self.screen.update()
        self.screen.geometry("{0}x{1}+0+0".format(
            self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()))
        self.width = self.screen.winfo_screenwidth()
        self.height = self.screen.winfo_screenheight()

        self.spacecraft_image = None
        self.spacecraft = None
        self.background = background
        self.spacecraft_bitmap = None
        self.planets = None
        self.filename = None
        self.background_filename = None
        self.planet_filenames = []

        self.masa = tkinter.Scale(self.screen, from_=1, to=30)
        self.masa.grid(row=0, column=0)
        self.pal = tkinter.Scale(self.screen, from_=0, to=100)
        self.pal.grid(row=0, column=1)
        self.kat = tkinter.Scale(self.screen, from_=0, to=359)
        self.kat.grid(row=0, column=2)
        self.szybkosc = tkinter.Scale(self.screen, from_=1, to=30)
        self.szybkosc.grid(row=0, column=3)
        self.st = tkinter.Button(self.screen, text="Start", command=self.start_sim)
        self.st.grid(row=0, column=5)

        self.canvas = tkinter.Canvas(self.screen, bg="black", height=self.height-130, width=self.width-60)
        self.canvas.bind("<Key>", self.key)
        self.screen.bind("<Key>", self.key)

        self.width = self.screen.winfo_screenwidth()-60
        self.height = self.screen.winfo_screenheight() -130

    def key(self, event):
        self.spacecraft.fly(self.planets, [event])

    def show_screen(self):
        self.screen.mainloop()

    def start_sim(self):
        self.spacecraft.mass = self.masa.get()
        self.spacecraft.fuel = self.pal.get()
        self.spacecraft.direction = self.kat.get()
        self.spacecraft.speed = self.szybkosc.get()
        self.move_spacecraft(GameController.flight(self.planets, self.spacecraft, self.width, self.height))

    def add_planet(self, planets):
        self.planets = planets
        for p in planets:
            x = p.coordinates.x
            y = p.coordinates.y
            self.planet_filenames.append(tkinter.PhotoImage(file=p.image))
            self.planet_filenames[-1] = self.planet_filenames[-1].subsample(int(125 / p.radius), int(125 / p.radius))
            self.canvas.create_image((x, y), image=self.planet_filenames[-1])

    def add_spacecraft(self, spacecraft):
        self.spacecraft = spacecraft
        self.spacecraft_image = Image.open(spacecraft.image)
        self.filename = ImageTk.PhotoImage(self.spacecraft_image.rotate(spacecraft.direction))
        self.spacecraft_bitmap = self.canvas.create_image((spacecraft.position.x, spacecraft.position.y),
                                                          image=self.filename)

    def move_spacecraft(self, movement_tuple):
        self.canvas.move(self.spacecraft_bitmap, movement_tuple[0], movement_tuple[1])
        self.rotate_spacecraft(movement_tuple[2])
        if GameController().is_dead(self.planets, self.spacecraft, self.width, self.height):
            self.canvas.delete(self.spacecraft_bitmap)
            self.show_gif()
            self.screen.destroy()
        elif GameController().has_won(spacecraft=self.spacecraft):
            self.show_won()
        else:
            self.canvas.after(100, self.move_spacecraft,
                              GameController.flight(self.planets, self.spacecraft, self.width, self.height))

    def rotate_spacecraft(self, direction):
        self.spacecraft_image = Image.open(self.spacecraft.image)
        self.filename = ImageTk.PhotoImage(self.spacecraft_image.rotate(direction))
        self.spacecraft_bitmap = self.canvas.create_image((self.spacecraft.position.x, self.spacecraft.position.y),
                                                          image=self.filename)
        self.spacecraft.direction = direction

    def pack_canvas(self, _planets, _spacecraft):
        self.canvas.grid(row=1, column=0, columnspan=6)
        self.set_background_image()
        self.add_planet(planets=_planets)
        self.add_spacecraft(spacecraft=_spacecraft)

    def set_background_image(self):
        self.background_filename = tkinter.PhotoImage(file=self.background)
        self.canvas.create_image(0, 0, image=self.background_filename, anchor="nw")

    def show_gif(self, f=200):
        try:
            self.filename = tkinter.PhotoImage(file=ImL.get_explosion_gif(), format="gif -index {}".format(f))
            self.spacecraft_bitmap = self.canvas.create_image(self.spacecraft.position.x, self.spacecraft.position.y,
                                                              image=self.filename)
            f += 1
        except Exception:
            f = 1
        self.canvas.after(100, self.show_gif, f)

    def show_won(self):
        messagebox.showinfo("Congratulation!", "You have won!")
