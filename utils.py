import os

def screen_cleaner():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

scores_file_name = "Scores.txt"
bad_return_code = 1000

