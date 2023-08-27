import game_field
import consts
import random
import pygame


def generate_teleport_locations(game_board):
    tp_location_list = []

    for _ in range(consts.NUM_OF_TP):
        y = random.randint(0, consts.NUM_OF_ROWS - 1)
        while not 0 <= y >= 3:
            y = random.randint(0, consts.NUM_OF_ROWS - 1)
        x = random.randint(0, consts.NUM_OF_COLS - consts.TP_BLOCKS_WIDTH - 1)
        for i in range(consts.TP_BLOCKS_WIDTH):
            game_board[y][x + i] = consts.TP
            tp_location_list.append([y, x + 1])
    return tp_location_list
