import random

import consts


# create the board list
def create_board():
    game_board = [[consts.FREE_SPACE for _ in range(consts.NUM_OF_COLS)] for _ in range(consts.NUM_OF_ROWS)]
    return game_board


# create the bushes location on board
def generate_bush_locations(game_board):
    for _ in range(consts.NUM_OF_BUSHES):
        x = random.randint(0, consts.NUM_OF_COLS - consts.TRAP_BLOCKS_WIDTH - 1)
        y = random.randint(0, consts.NUM_OF_ROWS - 1)
        game_board[y][x] = consts.BUSH


# create the traps location on board
def generate_trap_locations(game_board):
    for _ in range(consts.NUM_OF_TRAPS):
        x = random.randint(0, consts.NUM_OF_COLS - consts.TRAP_BLOCKS_WIDTH - 1)
        y = random.randint(0, consts.NUM_OF_ROWS - 1)
        for i in range(consts.TRAP_BLOCKS_WIDTH):
            game_board[y][x + i] = consts.TRAP


# putting the flag signs in the board of the game
def locate_flag(game_board):
    for i in range(12):
        game_board[consts.FLAG_LOCATION[i][0]][consts.FLAG_LOCATION[i][1]] = consts.FLAG