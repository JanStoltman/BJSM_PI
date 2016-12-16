import tkinter


class ScreenController:
    def __init__(self):
        self.screen = tkinter.Tk()
        self.screen.update()
        self.screen.geometry("{0}x{1}+0+0".format(
            self.screen.winfo_screenwidth() - 100,  self.screen.winfo_screenheight() - 100))
        self.width = self.screen.winfo_width()
        self.height = self.screen.winfo_height()

    def show_screen(self):
        self.screen.mainloop()
