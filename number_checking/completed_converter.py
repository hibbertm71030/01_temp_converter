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
        self.to_convert_entry = Entry(self.converter_frame, width=20, font=("Arial", "14", "bold"))
        self.to_convert_entry.grid(row=2)

        # conversion buttons
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Celsius", font=("Arial", "10"), bg="dark turquoise",
                                  padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font=("Arial", "10"), bg="tomato",
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
                                  text="Help", width=5, command=self.help)
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

                self.all_calculations.append(answer)
                self.history_button.config(state=NORMAL)

            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)


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

    def history(self, calc_history):
        History(self, calc_history)

    def help(self):
        print("you asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box then push one of "
                                          "the buttons to convert to celsius or fahrenheit"
                                          "\nThe calculation history shows up to 7 past calculations in order \n"
                                          "You can also export a full list of previous calculations to a text file via"
                                          " the export button in the history")


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
        self.export_button = Button(self.export_dismiss_frame, text="export",
                                    font="Arial 10", bg=background,
                                    command=lambda: self.export(calc_history))
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

        # error message labels
        self.save_error_label = Label(self.export_frame, text="", fg="maroon", bg=background)
        self.save_error_label.grid(row=4)

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

        # cross button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

    def save_history(self, partner, calc_history):

        # regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        problem = ""

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # display error
            self.save_error_label.config(text="invalid filename - {}".format(problem))
            # change entry box colour
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:

            # if there are no errors, generate text file and then close
            filename = filename + ".txt"

            # create file
            f = open(filename, "w+")

            # add heading
            f.write("Temperature Conversion History\n\n")

            # add new line at end of each item
            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialouge
            self.close_export(partner)

    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


class Help:
    def __init__(self, partner):
        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up little help window
        self.help_box = Toplevel()

        # help gui
        self.help_frame = Frame(self.help_box, bg=background, )
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

        # cross button
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
