import time
import pygame

import consts
import game_field
import Screen
import Soldier

global finish_game
global see_trap_mode
global game_board
global soldier


def pygame_keys_events():
    global see_trap_mode
    global finish_game
    global game_board
    global soldier

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                see_trap_mode = True
            if not see_trap_mode:
                if event.key == pygame.K_UP:
                    soldier_location = soldier.get_location()
                    game_board = soldier.update_location([soldier_location[0] - 1, soldier_location[1]])
                if event.key == pygame.K_DOWN:
                    soldier_location = soldier.get_location()
                    game_board = soldier.update_location([soldier_location[0] + 1, soldier_location[1]])
                if event.key == pygame.K_RIGHT:
                    soldier_location = soldier.get_location()
                    game_board = soldier.update_location([soldier_location[0], soldier_location[1] + 1])
                if event.key == pygame.K_LEFT:
                    soldier_location = soldier.get_location()
                    game_board = soldier.update_location([soldier_location[0], soldier_location[1] - 1])


def main():
    global finish_game
    global see_trap_mode
    global game_board
    global soldier

    see_trap_mode = False
    screen, clock = Screen.pygame_init()
    game_board = game_field.create_board()
    game_field.generate_bush_locations(game_board)
    game_field.generate_trap_locations(game_board)
    game_field.locate_flag(game_board)
    soldier = Soldier.Soldier(game_board, [0, 0])

    finish_game = False
    while not finish_game:
        if not see_trap_mode:
            Screen.display_screen(screen, game_board)
        else:
            Screen.display_night_vision_screen(screen, game_board)
            see_trap_mode = False
        pygame_keys_events()

        clock.tick(consts.REFRESH_RATE)


if __name__ == '__main__':
    main()
