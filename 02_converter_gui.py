from tkinter import *
import random
from functools import partial

class Converter:
    def __init__(self, parent):

        # formatting variables
        background_colour = "light green"

        # converter GUI
        self.converter_frame = Frame(width=500, height=500, bg=background_colour,
                                     pady=10)
        self.converter_frame.grid()

        # heading
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "18", "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # user instructions
        self.instructions = Label(self.converter_frame, text="type in temperature below then push one of the buttons",
                                          font=("Arial", "6"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.instructions.grid(row=1)






# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()