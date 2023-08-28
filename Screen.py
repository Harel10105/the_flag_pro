import time
import pygame

import consts


# pygame library init lines and return the pygame screen
def pygame_init():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("The Flag")
    screen = pygame.display.set_mode(consts.SCREEN_SIZE)
    clock = pygame.time.Clock()
    return screen, clock


# draw the regular screen
def display_screen(screen, game_board):
    img = pygame.image.load(consts.SCREEN_BACKGROUND_IMAGE)
    screen.blit(img, (0, 0))
    display_bushes(screen, game_board)
    display_soldier(screen, game_board, consts.SOLDIER_IMAGE)
    display_guard(screen, game_board)
    display_flag(screen)
    pygame.display.flip()
    pygame.display.update()


# draw the night - vision screen
def display_night_vision_screen(screen, game_board):
    screen.fill(consts.WHITE)
    img = pygame.image.load(consts.NIGHT_VISION_BACKGROUND)
    screen.blit(img, (0, 0))
    display_traps(screen, game_board)
    display_soldier(screen, game_board, consts.NIGHT_VISION_SOLDIER)
    display_teleports(screen, game_board)
    display_flag(screen)

    pygame.display.flip()
    pygame.display.update()
    time.sleep(1)


# draw any image of the game
def display_image(screen, path, size):
    img = pygame.image.load(path)
    img.set_colorkey(consts.REMOVE_COLOR)
    screen.blit(img, size)


# draw all the bushes
def display_bushes(screen, game_board):
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if game_board[row][col] == consts.BUSH:
                bush_location = (col * consts.SCREEN_BLOCK_WIDTH, row * consts.SCREEN_BLOCK_HEIGHT)
                display_image(screen, consts.BUSH_IMAGE, bush_location)


# draw all the traps
def display_traps(screen, game_board):
    for row in range(len(game_board)):
        draw_counter = 3
        for col in range(len(game_board[row])):
            if game_board[row][col] == consts.TRAP and draw_counter % 3 == 0:
                trap_location = (col * consts.SCREEN_BLOCK_WIDTH, row * consts.SCREEN_BLOCK_HEIGHT)
                display_image(screen, consts.BOMB_IMAGE, trap_location)
                draw_counter += 1
            elif game_board[row][col] != consts.TRAP:
                draw_counter = 3


# draw the soldier
def display_soldier(screen, game_board, soldier_img):
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if game_board[row][col] == consts.SOLDIER:
                soldier_location = (col * consts.SCREEN_BLOCK_WIDTH, row * consts.SCREEN_BLOCK_HEIGHT)
                display_image(screen, soldier_img, soldier_location)


# draw the flag
def display_flag(screen):
    flag_location = (
        consts.FLAG_LOCATION[0][1] * consts.SCREEN_BLOCK_HEIGHT, consts.FLAG_LOCATION[0][0] * consts.SCREEN_BLOCK_WIDTH)
    display_image(screen, consts.FLAG_IMAGE, flag_location)


# draw the teleports
def display_teleports(screen, game_board):
    for row in range(len(game_board)):
        counter = 3
        for col in range(len(game_board[row])):
            if game_board[row][col] == consts.TP and counter % 3 == 0:
                img = pygame.image.load(consts.TP_IMAGE)
                img.set_colorkey(consts.REMOVE_COLOR)
                screen.blit(img, (col * consts.SCREEN_BLOCK_WIDTH,
                                  row * consts.SCREEN_BLOCK_HEIGHT))
                counter += 1
            elif game_board[row][col] != consts.TP:
                counter = 3


# draw the guard
def display_guard(screen, game_board):
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if game_board[row][col] == consts.GUARD:
                display_image(screen, consts.GUARD_IMAGE, (col * consts.SCREEN_BLOCK_WIDTH,
                                                           consts.GUARD_LOCATION_HEIGHT * consts.SCREEN_BLOCK_HEIGHT))


# display wining screen
def display_win(screen):
    display_image(screen, consts.WIN_IMAGE, (0, 0))
    pygame.display.flip()
    time.sleep(3)


# display lose screen
def display_lose(screen, soldier, game_board):
    img = pygame.image.load(consts.SCREEN_BACKGROUND_IMAGE)
    screen.blit(img, (0, 0))
    display_bushes(screen, soldier.get_map())
    display_flag(screen)
    soldier_location = soldier.get_location()
    display_guard(screen, game_board)
    display_image(screen, consts.INJURY_IMAGE, (soldier_location[1] * consts.SCREEN_BLOCK_WIDTH,
                                                soldier_location[
                                                    0] * consts.SCREEN_BLOCK_HEIGHT - consts.SOLDIER_BLOCK_HEIGHT * 5))
    display_image(screen, consts.EXPLOSION_IMAGE, (
        soldier_location[1] * consts.SCREEN_BLOCK_WIDTH - consts.SCREEN_BLOCK_WIDTH / 2,
        soldier_location[0] * consts.SCREEN_BLOCK_HEIGHT))
    pygame.display.flip()
    time.sleep(3)
    display_image(screen, consts.LOSE_IMAGE, (0, 0))
    pygame.display.flip()
    time.sleep(3)
