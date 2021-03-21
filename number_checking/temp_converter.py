from tkinter import *
import random
from functools import partial

class Converter:
    def __init__(self, parent):

        # formatting variables
        background_colour = "light green"

        # calculation history list (WILL BE BLANK in actual program)
        self.all_calculations = []

        # converter GUI
        self.converter_frame = Frame(bg=background_colour,
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
                                  padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font=("Arial", "10"), bg="red",
                                  padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # History and help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.hist_help_frame, font=("Verdana", "10"),
                                     text="Calculation History", width=15,
                                     command=lambda: self.history(self.all_calculations))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calculations) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font=("Verdana", "10"),
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

        # Answer label
        self.converted_label = Label(self.converter_frame,
                                     font=("Verdana", "10"), fg="purple",
                                     bg=background_colour, pady=10,
                                     text="Conversion goes here")
        self.converted_label.grid(row=4)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"

        # Retrieve amount entered into entry field.
        to_convert = self.to_convert_entry.get()

        # Check amount is a valid number.
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check amount is a valid number

            # Convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert, celsius)

            else:
                answer = "too cold"
                has_errors = "yes"


            # display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add answer to list for history
            if answer != "too cold":
                self.all_calculations.append(answer)
                print(self.all_calculations)


        except ValueError:
            self.converted_label.configure(text="please enter a number", fg="red")
            self.to_convert_entry.configure(bg=error)

    # Round
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded







# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()