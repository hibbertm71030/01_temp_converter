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

        # export button
        self.export_button = Button(self.converter_frame, text="export",
                                  padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)


class Export:
    def __init__(self, partner):

        background = "orange"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # cross button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # sets up little export window
        self.export_box = Toplevel()

        # export gui
        self.export_frame = Frame(self.export_box, bg=background,)
        self.export_frame.grid()

        # export heading
        self.export_label = Label(self.export_frame, text="Export/instructions",
                                          font=("Arial", "13", "bold"),
                                          bg=background,
                                          padx=10, pady=10)
        self.export_label.grid(row=0)

        # export text
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below"
                                                         "and press the save button to save your calc"
                                                         "history to a text file.",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # warning text
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists"
                                                         " its content will be replaced by your calc history",
                                 justify=LEFT, width=40, bg="#ffafaf", fg="maroon", wrap=225,
                                 font="Arial 10 italic", padx=10, pady=10)
        self.export_text.grid(row=2)

        # filename entry box
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 12", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # save/cancel button
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # save/cancel buttons
        self.save_button = Button(self.save_cancel_frame, text="save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)



    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
