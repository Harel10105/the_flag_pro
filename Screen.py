import time
import pygame

import consts


# pygame library init lines and return the pygame screen
def pygame_init():
    pygame.init()
    pygame.display.set_caption("The Flag")
    screen = pygame.display.set_mode(consts.SCREEN_SIZE)
    clock = pygame.time.Clock()
    return screen, clock


# draw the regular screen
def display_screen(screen, game_board):
    screen.fill(consts.SCREEN_BACKGROUND)
    display_bushes(screen, game_board)
    display_soldier(screen, game_board, consts.SOLDIER_IMAGE)
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


# display wining screen
def display_win(screen):
    display_image(screen, consts.WIN_IMAGE, (0, 0))
    pygame.display.flip()
    time.sleep(3)


# display lose screen
def display_lose(screen):
    display_image(screen, consts.LOSE_IMAGE, (0, 0))
    pygame.display.flip()
    time.sleep(3)
