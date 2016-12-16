import tkinter


class ScreenController:
    def __init__(self):
        self.screen = tkinter.Tk()
        self.screen.update()
        self.screen.geometry("{0}x{1}+0+0".format(
            self.screen.winfo_screenwidth(),  self.screen.winfo_screenheight()))
        self.width = self.screen.winfo_screenwidth()
        self.height = self.screen.winfo_screenheight()
        self.canvas = tkinter.Canvas(self.screen, bg="black", height=self.height, width=self.width)
        self.canvas.pack()

    def show_screen(self):
        self.screen.mainloop()
