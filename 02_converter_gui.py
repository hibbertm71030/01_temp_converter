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
                                          font=("Arial", "10"), wrap=250,
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.instructions.grid(row=1)

        # entry box
        self.to_convert_entry = Entry(self.converter_frame, width=20,font=("Arial", "14", "bold"))
        self.to_convert_entry.grid(row=2)

        # conversion buttons
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Celsius", font=("Arial", "10"), bg="blue",
                                  padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font=("Arial", "10"), bg="red",
                                  padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()