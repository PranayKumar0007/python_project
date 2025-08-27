from art import logo
import random

print(logo)
print("WELCOME TO 'GUESS THE NUMBER'")
print("I am thinking of a number between 1 and 100")



def number_guess(chances):

    number = random.randint(1, 100)

    game_over = False
    while not game_over:
        guess = int(input(f"Guess the number between 1 and 100: "))


        if guess == number:
            game_over = True
            print("""You guessed the number correctly.
            YOU WIN!!!""")

        elif 1<= guess <= number:
            game_over = False
            chances -= 1
            print(f"""You guessed too low.
You have {chances } chances left to guess the number.""")
        elif number <= guess <= 100:
            game_over = False
            chances -= 1
            print(f"""You guessed too high.
You have {chances} chances left to guess the number.""")
        if chances == 0:
            game_over = True
            print("""You used up all your chances! 
Game over!!""")


def difficulty_chooser():
    difficulty = input("Choose a difficulty (easy, hard): ").lower()


    if difficulty == "easy":
        chances = 10
        print("You chose easy difficulty you now have 10 chances to guess the number.")
        number_guess(chances)
    if difficulty == "hard":
        chances = 5
        print("You chose hard difficulty you now have 5 chances to guess the number.")
        number_guess(chances)

difficulty_chooser()

while input("Do you want to play again? (y/n): ").lower() == "y":
    print("\n" * 20)
    print(logo)
    print("WELCOME TO 'GUESS THE NUMBER'")
    print("I am thinking of a number between 1 and 100")
    difficulty_chooser()
















