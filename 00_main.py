# imports
import random
import time

# Functions go here
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


# Main Routine

