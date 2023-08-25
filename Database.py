import pandas as pd

import consts


def save_data(key, game_board):
    save_dict = load_data(game_board)
    save_dict[str(key)] = game_board
    new = pd.DataFrame.from_dict(save_dict)
    new.to_csv("save_data.csv", index=False, header=True)


def load_data(game_board):
    game_states = pd.read_csv("save_data.csv")
    game_states["1"] = game_states["1"].apply(eval)
    game_states["2"] = game_states["2"].apply(eval)
    game_states["3"] = game_states["3"].apply(eval)
    game_states["4"] = game_states["4"].apply(eval)
    game_states["5"] = game_states["5"].apply(eval)
    game_states["6"] = game_states["6"].apply(eval)
    game_states["7"] = game_states["7"].apply(eval)
    game_states["8"] = game_states["8"].apply(eval)
    game_states["9"] = game_states["9"].apply(eval)
    save_dict = {"1": [game_states["1"].get(i) for i in range(consts.NUM_OF_ROWS)],
                 "2": [game_states["2"].get(i) for i in range(consts.NUM_OF_ROWS)],
                 "3": [game_states["3"].get(i) for i in range(consts.NUM_OF_ROWS)],
                 "4": [game_states["4"].get(i) for i in range(consts.NUM_OF_ROWS)],
                 "5": [game_states["5"].get(i) for i in range(consts.NUM_OF_ROWS)],
                 "6": [game_states["6"].get(i) for i in range(consts.NUM_OF_ROWS)],
                 "7": [game_states["7"].get(i) for i in range(consts.NUM_OF_ROWS)],
                 "8": [game_states["8"].get(i) for i in range(consts.NUM_OF_ROWS)],
                 "9": [game_states["9"].get(i) for i in range(consts.NUM_OF_ROWS)]}
    return save_dict


def load_data_for_game(key, game_board):
    current_game_data = load_data(game_board)[str(key)]
    return current_game_data
