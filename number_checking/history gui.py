from tkinter import *
import random
from functools import partial

class Converter:
    def __init__(self, parent):

        # formatting variables
        background_colour = "light green"

        # calculation history list (WILL BE BLANK in actual program)
        self.all_calculations = ['1 degrees F is -17.2 degrees C',
                                 '2 degrees F is -16.7 degrees C',
                                 '8 degrees F is -13.3 degrees C',
                                 '-10 degrees F is -23.3 degrees C',
                                 '-74 degrees F is -58.9 degrees C',
                                 '56 degrees F is 13.3 degrees C']

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

        # history button
        self.history_button = Button(self.converter_frame, text="history",
                                  padx=10, pady=10, command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        print("you asked for History")
        get_history = history(self)
        get_history.history_text.configure(text="History text goes here")

class history:
    def __init__(self, partner):

        background = "light blue"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up little history window
        self.history_box = Toplevel()

        # history gui
        self.history_frame = Frame(self.history_box, bg=background,)
        self.history_frame.grid()

        # history heading
        self.history_label = Label(self.history_frame, text="History/instructions",
                                          font=("Arial", "13", "bold"),
                                          bg=background,
                                          padx=10, pady=10)
        self.history_label.grid(row=0)

        # history text
        self.history_text = Label(self.history_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.history_text.grid(column=0, row=1)

        # export/dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="export", font="Arial 10", bg=background)
        self.export_button.grid(row=0, column=0)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="dismiss", font="Arial 10", bg=background,
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

        #cross button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

    def close_history(self, partner):
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
