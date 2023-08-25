import time
import pygame

import consts
import game_field
import Screen
import Soldier

global finish_game
global see_trap_mode


def pygame_keys_events(game_board):
    global see_trap_mode
    global finish_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                see_trap_mode = True



def main():
    see_trap_mode = False
    screen, clock = Screen.pygame_init()
    game_board = game_field.create_board()
    game_field.generate_bush_locations(game_board)
    game_field.generate_trap_locations(game_board)
    game_field.locate_flag(game_board)
    soldier = Soldier.Soldier(game_board, [0, 0])

    pygame_keys_events(game_board)
    finish_game = False
    while not finish_game:
        pygame_keys_events(game_board)
        if not see_trap_mode:
            Screen.display_screen(screen, game_board)
        else:
            Screen.display_night_vision_screen(screen, game_board)
            see_trap_mode = False

        clock.tick(consts.REFRESH_RATE)


if __name__ == '__main__':
    main()
