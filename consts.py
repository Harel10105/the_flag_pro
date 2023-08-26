# constants of pygame
REFRESH_RATE = 100

# constants of the symbols of the game map
FREE_SPACE = 'X'
SOLDIER = 'S'
TRAP = 'O'
FLAG = 'F'
BUSH = 'B'
TP = 'TP'

# constants of the game board settings
NUM_OF_ROWS = 25
NUM_OF_COLS = 50
WINDOW_HEIGHT = 500
WINDOW_WIDTH = WINDOW_HEIGHT * 2
SCREEN_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
SCREEN_BLOCK_WIDTH = WINDOW_WIDTH / NUM_OF_COLS
SCREEN_BLOCK_HEIGHT = WINDOW_HEIGHT / NUM_OF_ROWS
NUM_OF_BOMBS = 20
NUM_OF_BUSH = 20

FLAG_LOCATION = [(21, 46), (21, 47), (21, 48), (21, 49),
                 (22, 46), (22, 47), (22, 48), (22, 49),
                 (23, 46), (23, 47), (23, 48), (23, 49)]

# constants colors
BACKGROUND_COLOR = (118, 238, 0)  # GREEN
SCREEN_BACKGROUND = (32, 194, 0)
WHITE = (255, 255, 255)
REMOVE_COLOR = (183, 87, 175)

# constants of images path
BUSH_IMAGE = "images/grass.png"
SOLDIER_IMAGE = "images/soldier.png"
FLAG_IMAGE = "images/flag.png"
BOMB_IMAGE = "images/bomb.png"
INJURY_IMAGE = "images/injury.png"
EXPLOSION_IMAGE = "images/explotion.png"
NIGHT_VISION_BACKGROUND = "images/Final_lazer-net.png"
NIGHT_VISION_SOLDIER = "images/soldier_nigth.png"
WIN_IMAGE = "images/youWin.png"
LOSE_IMAGE = "images/game_over.png"

# constants of bushes settings
NUM_OF_BUSHES = 20
BUSH_HEIGHT = 40
BUSH_WIDTH = 60

# constants of traps/bombs settings
NUM_OF_TRAPS = 20
TRAP_BLOCKS_WIDTH = 3
TRAP_HEIGHT = WINDOW_HEIGHT / NUM_OF_ROWS
TRAP_WIDTH = (WINDOW_WIDTH / NUM_OF_COLS) * TRAP_BLOCKS_WIDTH
DETECT_BOMBS_SEC = 1

# constants of soldier settings
SOLDIER_BLOCK_HEIGHT = 4
SOLDIER_BLOCK_WIDTH = 2
SOLDIER_WIDTH = SOLDIER_BLOCK_WIDTH * SCREEN_BLOCK_WIDTH
SOLDIER_HEIGHT = SOLDIER_BLOCK_HEIGHT * SCREEN_BLOCK_HEIGHT

# constants of teleport settings
NUM_OF_TP = 5
