import random
import os
import time

def generate_sequence(difficulty):
    rundom_numbers = [random.randint(1,101) for i in range(0, difficulty)]
    print(rundom_numbers)
    time.sleep(1)
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    return(rundom_numbers)

def get_list_from_user(difficulty):
    user_list = []
    for i in range(int(difficulty)):
        number = int(input(f"Enter number {i+1}: "))
        user_list.append(number)
    return (user_list)


def is_list_equal(sequence, user_list):
    user_win = (sequence == user_list)
    return (user_win)


def play(difficulty):
    sequence = generate_sequence(int(difficulty))
    user_list = get_list_from_user(difficulty)
    game_result = is_list_equal(sequence, user_list)
    return(game_result)
