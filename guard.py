import consts


# moving the guard function
def move_guard(guard_location, is_guard_move_left):
    if check_guard_boarder(guard_location, is_guard_move_left):
        if is_guard_move_left:
            guard_location = [guard_location[0], guard_location[1] - 1]
        else:
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
