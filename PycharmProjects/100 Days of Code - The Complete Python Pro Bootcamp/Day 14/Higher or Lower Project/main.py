from game_data import data
import random
from art import logo, vs


# Return a random account and its formatted string and followers
def random_picker():
    choice = random.choice(data)
    name = choice['name']
    description = choice['description']
    country = choice['country']
    followers = choice['follower_count']
    return {
        "info": f"{name}, a {description}, from {country}",
        "followers": followers
    }


def game():

    score = 0

    # Get initial two choices
    choice_a = random_picker()
    choice_b = random_picker()
    # Avoid duplicates
    while choice_a['info'] == choice_b['info']:
        choice_b = random_picker()

    game_continue = True

    while game_continue:

        print(logo)
        print(f"Compare A: {choice_a['info']}")
        print(vs)
        print(f"Against B: {choice_b['info']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = choice_a['followers']
        b_followers = choice_b['followers']

        # Determine if user is correct
        is_correct = False
        if guess == 'a' and a_followers > b_followers:
            is_correct = True
        elif guess == 'b' and b_followers > a_followers:
            is_correct = True

        if is_correct:
            score += 1
            print("\n"*20)
            print(f"You're right! Current score: {score}.")
            # Winner becomes the next A
            if guess == 'a':
                choice_b = random_picker()
                while choice_a['info'] == choice_b['info']:
                    choice_b = random_picker()
            else:
                choice_a = choice_b
                choice_b = random_picker()
                while choice_a['info'] == choice_b['info']:
                    choice_b = random_picker()
        else:
            game_continue = False
            print(f"You're Wrong! Final score: {score}")


# Run the game
game()

#for shifting choice b to a if player got it right

