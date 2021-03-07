# code to check if number is valid...

def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("enter a number: "))

            if response < low:
                print("Too cold")
            else:
                return response

        except ValueError:
            print("please enter a number")


# main routine
number = temp_check(-273)
print("you chose {}".format(number))

number = temp_check(-459)
print("you chose {}".format(number))