from Data import data
import Art
import random


def get_random_account():
    return random.choice(data)


def get_formatted_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def compare(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'a'
    elif followers_b > followers_a:
        return guess == 'b'


def game():
    print(Art.logo)
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()
    game_continue = True
    while game_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A:{get_formatted_data(account_a)}")
        print(Art.vs)
        print(f"Against B:{get_formatted_data(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        check = compare(guess, a_follower_count,b_follower_count)

        if check:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
