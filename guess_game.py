import random

def generate_number(difficulty):
    return (random.randrange(0, int(difficulty)))

def get_guess_from_user(difficulty):
    return (input(f"Enter a number between 0 to {difficulty} : "))

def compare_results(secret_number, number_from_user):
    if (int(secret_number) == int(number_from_user)):
        user_win = True
    else:
        user_win = False
    return (user_win)

def play(difficulty):
    secret_number = generate_number(difficulty)
    number_from_user = get_guess_from_user(difficulty)
    game_result = compare_results(secret_number, number_from_user)
    return(game_result)