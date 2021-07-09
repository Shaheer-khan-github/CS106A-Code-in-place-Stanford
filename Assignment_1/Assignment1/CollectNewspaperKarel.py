from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    # your code here...
    Column_moving()
    Change_Direction()
    if front_is_blocked():
        turn_left()
        move()
        Testing()

        while front_is_blocked():
            turn_left()
            move()
            #         turn_left()
            Testing()

    ##############--Testing--###################


def Testing():
    while front_is_clear():
        Column_moving()
        Change_Direction()

    ##############--Direction_Change--###################


def Change_Direction():
    front_testing()


def front_testing():
    while front_is_blocked():
        if beepers_present():
            turn_right()
            move()
            turn_right()

    if no_beepers_present():
        until_wall_blocked()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

    ##################--COLUMN--#####################


def Column_moving():
    turn_left()
    until_wall_blocked()


def until_wall_blocked():
    while front_is_clear():
        put_beeper_in_row()


def put_beeper_in_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
