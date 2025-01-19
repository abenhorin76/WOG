from apps import start_play, welcome
import memory_game, guess_game, currency_roulette_game, utils, score
from score import add_score

welcome()
start_play()

# user_win = ""
#
# # running the Memory game
# if (int(game_selection) == 1):
#     user_win = memory_game.play(difficulty_selection)
#
# # running the Guess Game
# if (int(game_selection) == 2):
#     user_win = guess_game.play(difficulty_selection)
#
# # running the Currency Roulette game
# if (int(game_selection) == 3):
#     user_win = currency_roulette_game.play(difficulty_selection)
#
#
# add_score(difficulty_selection, user_win, utils.scores_file_name)