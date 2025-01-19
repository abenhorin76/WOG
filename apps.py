import memory_game, currency_roulette_game,guess_game, score, utils

def welcome():
    username = input('Please enter your name: ')
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey')


def start_play():
       game_check = False
       while not game_check:
           game_selection = input('Please choose a game to play:\n'
                           '1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back.\n'
                           '2. Guess Game - guess a number and see if you chose like the computer\n'
                           '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'
                           'Your Selection: ')
           if game_selection.isalpha():
               print("Please enter number only")
           else:
               int_game_selection = int(game_selection)
               if int_game_selection < 1 or int_game_selection > 3:
                print("Please choose a number between 1 to 3")
               else:
                 game_check = True

       difficulty_check = False
       while not difficulty_check:
           difficulty_selection = input('Please select difficulty level (1-5): ')
           if difficulty_selection.isalpha():
               print("Please enter number only")
           else:
               int_difficulty_selection = int(difficulty_selection)
               if int_difficulty_selection < 1 or int_difficulty_selection > 5:
                   print("Please enter a number between 1 to 5")
               else:
                    difficulty_check = True
       if (int(game_selection) == 1):
           user_win = memory_game.play(difficulty_selection)

       # running the Guess Game
       if (int(game_selection) == 2):
           user_win = guess_game.play(difficulty_selection)

       # running the Currency Roulette game
       if (int(game_selection) == 3):
           user_win = currency_roulette_game.play(difficulty_selection)

       if user_win:
           score.add_score(difficulty_selection, user_win, utils.scores_file_name)


