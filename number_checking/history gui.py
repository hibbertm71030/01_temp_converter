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
                                ]

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
        self.history_button = Button(self.converter_frame, text="history", padx=10, pady=10,
                                     command=lambda: self.history(self.all_calculations))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):

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
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations,"
                                                           " to save all your calculations press export.",
                                 font="arial 10", justify=LEFT, width=40, bg=background, wrap=250)
        self.history_text.grid(column=0, row=1)

        # generate string from calc list
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation history, "
                                              "you can save this data by pressing export.")

        # calc history label
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 10", justify=LEFT)
        self.calc_label.grid(row=2)

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

    def export(self, calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)

        background = "orange"

        # disable export button
        partner.export_button.config(state=DISABLED)

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
        self.save_button = Button(self.save_cancel_frame, text="save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

        def save_history(self, partner, calc_history)

        #cross button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
