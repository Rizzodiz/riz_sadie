# imports
import pandas

# functions go here
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


# yes no list
yes_no_list = [
    ["yes", "y"],
    ["no", "n"]
]


# main routine
fmk_function()