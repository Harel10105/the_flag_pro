import time
import keyboard as keyboard
import pygame

import Database
import consts
import game_field
import Screen
import Soldier
import guard
import teleport

# globals of the game
global finish_game
global see_trap_mode
global game_board
global soldier
global guard_location


# check player keyboard input
def pygame_keys_events(screen):
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
            # save and load game board for every key (1-9)
            if event.key == pygame.K_1:
                t = check_press_time()
                game_board = save_or_load(t, 1, screen)

            if event.key == pygame.K_2:
                t = check_press_time()
                game_board = save_or_load(t, 2, screen)

            if event.key == pygame.K_3:
                t = check_press_time()
                game_board = save_or_load(t, 3, screen)

            if event.key == pygame.K_4:
                t = check_press_time()
                game_board = save_or_load(t, 4, screen)

            if event.key == pygame.K_5:
                t = check_press_time()
                game_board = save_or_load(t, 5, screen)

            if event.key == pygame.K_6:
                t = check_press_time()
                game_board = save_or_load(t, 6, screen)

            if event.key == pygame.K_7:
                t = check_press_time()
                game_board = save_or_load(t, 7, screen)

            if event.key == pygame.K_8:
                t = check_press_time()
                game_board = save_or_load(t, 8, screen)

            if event.key == pygame.K_9:
                t = check_press_time()
                game_board = save_or_load(t, 9, screen)

            # move the soldier by keyboard
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


# check the length of the click
def check_press_time():
    t = time.time()  # Getting time in sec
    b = keyboard.read_event()
    while not b.event_type == "up":
        b = keyboard.read_event()
    print('Pressed Key "' + b.name + '" for ' + str(time.time() - t))
    return time.time() - t


# save or load the game board of the game from or to the database
def save_or_load(time_pressed, key, screen):
    global game_board
    global soldier
    global guard_location

    if time_pressed > 1:
        Database.save_data(key, game_board)
    else:
        game_board = Database.load_data_for_game(key, game_board)
        guard_location = guard.find_guard(game_board)
        soldier.set_map(game_board)
        Screen.display_screen(screen, soldier.get_map())
        print(game_board)
    return game_board


# main game loop
def main():
    global finish_game
    global see_trap_mode
    global game_board
    global soldier
    global guard_location

    screen, clock = Screen.pygame_init()
    game_board = game_field.create_board()

    game_field.generate_bush_locations(game_board)
    game_field.generate_trap_locations(game_board)
    game_field.locate_flag(game_board)
    tp_location_list = teleport.generate_teleport_locations(game_board)

    soldier = Soldier.Soldier(game_board, [0, 0])
    guard_location = [int(consts.NUM_OF_ROWS / 2) - 1, consts.NUM_OF_COLS - 1]

    trap_sound = pygame.mixer.Sound(consts.BOMB_SOUND)

    see_trap_mode = False
    is_guard_move_left = True
    gourd_walk_counter = 1
    normal_speed = consts.GUARD_MOVE_SPEED
    angry_guard_speed = consts.GUARD_MOVE_SPEED_ANGRY

    guard_speed = normal_speed
    finish_game = False
    while not finish_game:
        if not see_trap_mode:
            if gourd_walk_counter % guard_speed == 0:
                game_board[guard_location[0]][guard_location[1]] = consts.FREE_SPACE
                guard_location, is_guard_move_left = guard.move_guard(guard_location, is_guard_move_left, soldier)
                game_board[guard_location[0]][guard_location[1]] = consts.GUARD
                if guard.is_guard_angry(guard_location, soldier.get_location(), is_guard_move_left):
                    guard_speed = angry_guard_speed
                else:
                    guard_speed = normal_speed
                soldier.set_map(game_board)
            Screen.display_screen(screen, game_board)
            gourd_walk_counter += 1
            game_board = soldier.is_touch_tp(game_board, tp_location_list)
        else:
            Screen.display_night_vision_screen(screen, game_board)
            see_trap_mode = False

        # lose conditions
        if soldier.is_touch_trap() or soldier.is_touch_guard():
            trap_sound.play()
            Screen.display_lose(screen, soldier, game_board)
            finish_game = True
        # win condition
        elif soldier.is_touch_flag():
            Screen.display_win(screen)
            finish_game = True
        pygame_keys_events(screen)

        clock.tick(consts.REFRESH_RATE)


# game run
if __name__ == '__main__':
    main()
