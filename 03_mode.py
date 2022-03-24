# functions
import time


# Gives statements decoration on sides and top
def statement_generator(statement, side_decoration, top_bottom_decoration):

    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()



# main routine
modes_list = [
    'Wheel of Activities',
    'Fuck, Marry, Kill'
]

# display modes
statement_generator("Welcome Sadie and Rizzo", "~", "-")
time.sleep(1)
print('''
Choose a mode (1 - 2):''')
time.sleep(0.5)
print()

# initialise variable
mode_select = 1
for i in modes_list:
    print("{}: {}".format(mode_select, i))
    mode_select += 1
    time.sleep(0.05)
print()

while 1 == 1:
    mode_select = num_check("Choice:   ", "<error> please chose a number indicating a mode", int, 0, 3)
    print(mode_select)
