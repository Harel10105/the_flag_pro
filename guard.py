import consts
import Soldier
import main

global current_guard_image
current_guard_image = consts.NORMAL_GUARD_LEFT_IMAGE


# moving the guard function
def move_guard(guard_location, is_guard_move_left, soldier):
    global current_guard_image
    if check_guard_boarder(guard_location, is_guard_move_left):
        if is_guard_move_left:
            if is_guard_angry(guard_location, soldier.get_location(), is_guard_move_left):
                current_guard_image = consts.ANGRY_GUARD_LEFT_IMAGE
            else:
                current_guard_image = consts.NORMAL_GUARD_LEFT_IMAGE
            guard_location = [guard_location[0], guard_location[1] - 1]
        else:
            if is_guard_angry(guard_location, soldier.get_location(), is_guard_move_left):
                current_guard_image = consts.ANGRY_GUARD_RIGHT_IMAGE
            else:
                current_guard_image = consts.NORMAL_GUARD_RIGHT_IMAGE
            guard_location = [guard_location[0], guard_location[1] + 1]
    else:
        is_guard_move_left = not is_guard_move_left
        if is_guard_move_left:
            guard_location = [int(consts.NUM_OF_ROWS / 2) - 1, consts.NUM_OF_COLS - 1]
        else:
            guard_location = [int(consts.NUM_OF_ROWS / 2) - 1, 0]

    return guard_location, is_guard_move_left


def check_guard_boarder(guard_location, is_guard_move_left):
    if is_guard_move_left:
        if guard_location[1] - 1 == 0:
            return False
    else:
        if guard_location[1] + 1 == consts.NUM_OF_COLS:
            return False
    return True


# find the guard location
def find_guard(game_board):
    for row in range(consts.NUM_OF_ROWS):
        for col in range(consts.NUM_OF_COLS):
            if game_board[row][col] == consts.GUARD:
                return [row, col]


def is_guard_angry(guard_location, soldier_location, is_guard_move_left):
    if soldier_location[0] - 1 < consts.GUARD_LOCATION_HEIGHT < soldier_location[0] + 4:

        if soldier_location[1] < guard_location[1] and is_guard_move_left:
            return True
        if soldier_location[1] > guard_location[1] and not is_guard_move_left:
            return True
    return False
