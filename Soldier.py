import consts


class Soldier:
    """
    this class is for the soldier character.
    The values that the class save is the soldier's map and his location
    """
    def __init__(self, game_map, start_location):
        self._soldier_location = start_location
        self._game_map = game_map
        self._game_map[self._soldier_location[0]][self._soldier_location[1]] = consts.SOLDIER

    # getting the soldier's location
    def get_location(self):
        return self._soldier_location

    # getting the soldier's map
    def get_map(self):
        return self._game_map

    # updating the soldier's map
    def set_map(self, game_board):
        self._game_map = game_board
        self.__find_me()

    # updating the location of the soldier
    def update_location(self, new_location):
        if self.__is_next_step_on_board(new_location):
            self._game_map[self._soldier_location[0]][self._soldier_location[1]] = consts.FREE_SPACE
            self._game_map[new_location[0]][new_location[1]] = consts.SOLDIER
            self._soldier_location = new_location
        return self._game_map

    # Check if Soldier's next move is on board:
    @staticmethod
    def __is_next_step_on_board(next_location):
        if (next_location[0] > consts.NUM_OF_ROWS - consts.SOLDIER_BLOCK_HEIGHT) \
                or (next_location[1] > consts.NUM_OF_COLS - consts.SOLDIER_BLOCK_WIDTH) \
                or (next_location[0] < 0) or (next_location[1] < 0):
            return False
        return True

    # check if the soldier touch a trap
    def is_touch_trap(self):
        if (self._game_map[self._soldier_location[0] + 3][self._soldier_location[1]] == consts.TRAP) or \
                (self._game_map[self._soldier_location[0] + 3][self._soldier_location[1] + 1] == consts.TRAP):
            return True
        return False

    # check if the soldier touch the flag
    def is_touch_flag(self):
        if (self._game_map[self._soldier_location[0] + 3][self._soldier_location[1]] == consts.FLAG) or \
                (self._game_map[self._soldier_location[0] + 3][self._soldier_location[1] + 1] == consts.FLAG):
            return True
        return False

    # find the coordinates of the soldier on the map [y,x]
    def __find_me(self):
        for row in range(len(self._game_map)):
            for col in range(len(self._game_map[row])):
                if self._game_map[row][col] == consts.SOLDIER:
                    self._soldier_location = [row, col]



