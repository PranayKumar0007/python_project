rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player_game = input("Choose one. Rock, Paper or Scissors").lower()
if player_game == "rock":
    print(rock)
    print("You chose rock")
if player_game == "paper":
    print(paper)
    print("You chose paper")
if player_game == "scissors":
    print(scissors)
    print("You chose scissors")


game = [rock, paper, scissors]
import random
randomgame = random.randint(0,2)
print(game[randomgame])
if  randomgame== 0 :
    print("Computer chose rock")

if randomgame == 2 :
    print("Computer chose scissors")
if randomgame  == 1 :
    print("Computer chose paper")

if randomgame == 0 and player_game == "paper":
    print("You win")

if randomgame == 1 and player_game == "scissors":
    print("You win")
if randomgame == 2 and player_game == "rock":
    print("You win")

if randomgame == 0 and player_game == "scissors":
    print("You lose")
if randomgame == 1 and player_game == "rock":
    print("You lose")
if randomgame == 2 and player_game == "paper":
    print("You lose")
else:
    print("It's a draw")
