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

        # help button
        self.help_button = Button(self.converter_frame, text="help",
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("you asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="help text goes here")

class Help:
    def __init__(self, partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up little help window
        self.help_box = Toplevel()

        # help gui
        self.help_frame = Frame(self.help_box, bg=background,)
        self.help_frame.grid()

        # help heading
        self.help_label = Label(self.help_frame, text="Help/instructions",
                                          font=("Arial", "13", "bold"),
                                          bg=background,
                                          padx=10, pady=10)
        self.help_label.grid(row=0)

        # help text
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        # dismiss button
        self.dismiss_btn = Button(self.help_frame, text="dismiss",
                                  width=10, bg="orange", font="arial 10",
                                command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

        #cross button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
