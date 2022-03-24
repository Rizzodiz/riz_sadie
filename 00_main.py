# imports
import random
import time
import pandas

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


# Main Routine
# yes no list
yes_no_list = [
    ["yes", "y"],
    ["no", "n"]
]


# main routine
modes_list = [
    'Wheel of Activities',
    'Fuck, Marry, Kill'
]

seaaion_states_list = [
    'continue',
    'end'
]

# display modes and welcome message
statement_generator("Welcome Sadie and Rizzo", "~", "-")
time.sleep(1)

# session start
session = ''
while session != 'end':
    print('''
Choose a mode (1 - 2):
    ''')
    time.sleep(0.5)

    # initialise variable
    mode_select = 1
    for i in modes_list:
        print("{}: {}".format(mode_select, i))
        mode_select += 1
        time.sleep(0.05)
    print()

    
    mode_select = num_check("Choice:   ", "<error> please chose a number indicating a mode", int, 0, 3)
    print()
    
    # play mode the=at is selected
    if mode_select == 1:
        activity_generator()

    elif mode_select == 2:
        fmk_function()

    print()
    # once mode finished 
    session = string_checker("Continue Session? ", "<error> please enter 'continue' or 'end'.", seaaion_states_list)
    if session == "continue":
        statement_generator('Lets Go', '!', "=")
    
statement_generator("Goodbye", ":", "-")