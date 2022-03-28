# imports
import random
import time
import pandas
from turtle import *

# Functions go here
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


# checks if string is valid
def string_checker(question, error, options):

    valid = False
    while not valid:

        try:
            response = input(question)
            # if the snack is in one of the lists
            if response in options:
                return response
            
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()
    

# activity function
def activity_generator():
    # list of activities
    activities_list = [
        "Truth or Dare",
        "Clash Royale",
        "Skribble",
        "Fuck, Marry, Kill",
        "Would you Rather",
        "Turn on Cameras",
        "Just Chat ;)",
        "Grtic Phone",
        "Geoguesser",
        "turn each other on ;)"
    ]

    statement_generator("Wheel of Activities", "/", "=")
    print()

    activity = random.choice(activities_list)
    time.sleep(2)

    print('Which activity will be chosen...')
    print()
    time.sleep(3)

    statement_generator(activity, "!", "-")


# Gives statements decoration on sides and top
def statement_generator(statement, side_decoration, top_bottom_decoration):

    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# function of the fmk game
def fmk_function():
    '''Fmk docstring'''
    # display rules
    print("""rules""")
    print()

    # initialise lists
    rounds = []
    fuck = []
    marry = []
    kill = []

    # data dictionary
    fmk_data_dict = {
        'Round': rounds,
        'Fuck': fuck,
        'Marry': marry,
        'Kill': kill
    }

    # initialise variables
    fmk_count = 1

    # checks if user wants to play fmk
    fmk = ''
    while fmk != 'end':

        statement_generator("Welcom to Fuck, Marry, Kill", "/", "=")
        print()
        
        # figure out whos round it is..
        if (fmk_count % 2) == 0:
            print("Sadies Round")
            print("Ryan picks Options")
            rounds.append("Sadie, {}:".format(fmk_count))
        else:
            print("Ryans Round")
            print("Sadie picks Options")
            rounds.append("Ryan, {}:".format(fmk_count))
        print()
        
        names_list = []

        # ask user for the three names and append names
        for i in range(0, 3):
            name = input("Chose an Option: ")
            names_list.append(name)

        # print names
        print()
        print("Names:")
        for item in names_list:
            print("- {}".format(item))
        print()

        # ask user who they would fuck
        fucks = string_checker("Who would you have Sex with ;)? ", "Thats not an option", names_list)
        fuck.append(fucks)
        print()

        # remove option from list
        names_list.remove(fucks)

        # asks user who they would like to marry 
        marrys = string_checker("Who would you marry? ", "Thats not an option", names_list)
        marry.append(marrys)
        print()

        # remove option from list and print who dies
        names_list.remove(marrys)
        dies = names_list[0]
        print("So that leaves {} to die.".format(dies))
        kill.append(dies)
        print()

        # clear naes list and add to count
        names_list.clear
        fmk_count += 1

        fmk = input("Continue? ")
        
    print()
    statement_generator('RESULTS', "!", "-")
    print()
    # display data
    fmk_data_frame = pandas.DataFrame(fmk_data_dict)
    fmk_data_frame = fmk_data_frame.set_index('Round')

    fmk_data_frame = fmk_data_frame.reindex(columns=['Fuck', 'Marry', 'Kill'])
    print(fmk_data_frame)

    return fmk_data_frame


# heart function
def heart():
    '''heart docstring'''
    pendown()
    begin_fill()
    fillcolor('red')
    left(135)
    forward(140)
    circle(-70, 180)
    setheading(45)
    circle(-70, 180)
    forward(140)
    end_fill()


# 'i' function
def i_draw():
    '''i docstring'''
    pendown()
    begin_fill()
    fillcolor('black')
    setheading(90)
    forward(220)
    setheading(0)
    forward(40)
    setheading(270)
    forward(220)
    setheading(180)
    forward(40)   
    end_fill()


# 'u' function
def u_draw():
    '''u docstring'''
    pendown()
    begin_fill()
    fillcolor('black')
    setheading(270)
    forward(160)
    circle(80, 180)
    forward(160)
    setheading(180)
    forward(40)
    setheading(270)
    forward(150)
    circle(-40, 180)
    forward(150)   
    setheading(180)
    forward(40)
    end_fill()



# Main Routine
# yes no list
yes_no_list = ["yes", "no"]

modes_list = [
    'Wheel of Activities',
    'Fuck, Marry, Kill',
    'Secret ;)'
]

# display modes and welcome message
statement_generator("Welcome Sadie and Rizzo", "~", "-")
time.sleep(1)

# session start
session = ''
while session != 'end':
    print('''
Choose a mode (1 - 3):
    ''')
    time.sleep(0.5)

    # initialise variable
    mode_select = 1
    for i in modes_list:
        print("{}: {}".format(mode_select, i))
        mode_select += 1
        time.sleep(0.05)
    print()

    
    mode_select = num_check("Choice:   ", "<error> please chose a number indicating a mode", int, 0, 4)
    print()
    
    # play mode the=at is selected
    if mode_select == 1:
        activity_generator()

    elif mode_select == 2:
        fmk_function()

    elif mode_select == 3:
        # define turtle colours
        bgcolor('white')
        pensize(3)
        color('black')
        time.sleep(3)
        
        # draw heart
        goto(0, -100)
        heart()
        penup()

        # draw 'i'
        goto(-150, -100)
        i_draw()
        penup()

        # draw 'u'
        goto(100, 110)
        u_draw()
        time.sleep(3)


    print()
    # once mode finished 
    session = string_checker("Continue Session? ", "<error> please enter yes / no.", yes_no_list)
    if session == "yes":
        statement_generator('Lets Go', '!', "=")
    
    else:
        session = 'end'
    
statement_generator("Goodbye", ":", "-")