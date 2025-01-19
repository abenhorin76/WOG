import requests
import random

def get_money_interval(difficulty):
    response_api = requests.get("https://open.er-api.com/v6/latest/USD")
    data = response_api.json()
    if "rates" in data and "ILS" in data["rates"]:
        rate_shekel = round (data["rates"]["ILS"],2)
        acceptable_difference = 10 - int(difficulty)
    return(rate_shekel, acceptable_difference)

def get_guess_from_user():
    guess_number = random.randrange(1, 100, 1)
    check_user_input= False
    while not check_user_input:
        guess_from_user = input(f"Please guess the value of ${guess_number} in Isreali Shekel: ")
        if guess_from_user.isalpha():
            print("Please enter a number")
        else:
            check_user_input = True
            return (guess_number,guess_from_user)

def compare_results(rate, diff, num_dolar, guess):
     shekel_calc = num_dolar * rate
     guess = float(guess)
     if shekel_calc+diff >= guess >= shekel_calc-diff:
         user_win = True
     else:
         user_win = False
     return (user_win)

def play(difficulty):
    """

    :rtype: object
    """
    result_get_money_interval = get_money_interval(difficulty)
    num_from_user = get_guess_from_user()
    game_result = compare_results(result_get_money_interval[0], result_get_money_interval[1], num_from_user[0], num_from_user[1])
    return(game_result)





