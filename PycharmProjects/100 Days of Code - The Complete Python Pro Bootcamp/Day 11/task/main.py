from art import *
import random

###Mistakes  1. converting the already integer values of the list to strings.
#            2.using += to add the string values to list
#            3.naming a new variable and again converting the added string variables to integers and adding them to it
    #          which was unnecessary.
#            others errors summarised by chatgpt
 #           4. I also missed some of the special conditions in the game like the changing values of ace which I will be adding.
 #           5. didnt consider the logic by which the computer has to play the game. Computer wins even if its cards go above 21
###  Learnings:
 #   1.Used get_hand_total(hand) instead of get_hand_total(player_cards) which did not make much of a difference but was recommended by chat gpt
#    2.card_numbering()	Removed, not needed this function was unnecessary as it changed the set of player or c cards into integers which wasnt needed
 #   3.String appending cards	Changed to .append() . Used += which actually needs both the sets to be converted as strings
 #     using append we can directly add the cards to the list
 #     as they are already a list of integers
  #  4.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_or_quit():
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        print(logo)
        print("Welcome to the Black Jack!")
        card_picker()
    else:
        print("End of Game")


def get_hand_total(hand):
    ### added the next two if conditionals seeing the video
    if sum(hand) == 21 and len(hand) == 2:
        print("BLACKJACK!")
        play_or_quit()
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

 # Output: 23








def card_picker():
    player_cards = []
    computer_cards = []
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    player_cards += card1, card2
    print(f"Your hand : {player_cards}")
    cc1 = random.choice(cards)
    cc2 = random.choice(cards)
    computer_cards += cc1, cc2
    print(f"Computer hand : [{cc1},?]")

    hit = input("Do you want to pick another card? (y/n): ").lower()
    if hit == "y":
        hit_again = True
        while hit_again:
            cardnew = random.choice(cards)
            player_cards.append(cardnew)
            cardnewc = random.choice(cards)
            computer_cards.append(cardnewc)
            # added the computer rule the first one

            if get_hand_total(computer_cards) > 21:
                hit_again = False
                print(f"""Computer went over!!
                          Your hand : {player_cards}   Computer hand : [{computer_cards}]
                          Your score: {get_hand_total(player_cards)} computer score: {computer_cards}""")
            elif get_hand_total(player_cards) > 21:
                hit_again = False
                print(f"""Oh no!You went over!!  Your cards:{player_cards} 
                                                 Computer cards:{computer_cards} 
                      Your score is {get_hand_total(player_cards)}""")
                print("You lose!")
                play_or_quit()
            elif get_hand_total(player_cards) > get_hand_total(computer_cards) :
                hit_again = False
                print(f"""You win!!
                     Your cards:{player_cards}          computer cards:{computer_cards}
                
                      Your score : {get_hand_total(player_cards)} and Computer score : {get_hand_total(computer_cards)}""")
                play_or_quit()
            elif get_hand_total(player_cards) < get_hand_total(computer_cards) :
                hit_again = False
                print(f"""Computer wins!!  
                      Your cards:{player_cards}          computer cards:{computer_cards} 
                      Your score : {get_hand_total(player_cards)} and Computer score : {get_hand_total(computer_cards)}""")
                play_or_quit()
            elif get_hand_total(player_cards) == get_hand_total(computer_cards) :
                hit_again = False
                print(f"""It's a tie!  
                      Your cards:{player_cards}          computer cards:{computer_cards} 
                      Your score : {get_hand_total(player_cards)} and Computer score : {get_hand_total(computer_cards)}""" )

                play_or_quit()
    else:
        hit_again = False
        #added the computer rules
        if get_hand_total(computer_cards) > 21:

            print(f"""Computer went over!!
                      Your hand : {player_cards}   Computer hand : [{computer_cards}]
                      Your score: {get_hand_total(player_cards)} computer score: {computer_cards}""")
        elif get_hand_total(player_cards) > 21:

            print(f"""Oh no!You went over!!  Your cards:{player_cards} 
                                             Computer cards:{computer_cards} 
                  Your score is {get_hand_total(player_cards)}""")
            print("You lose!")
            play_or_quit()
        elif get_hand_total(player_cards) > get_hand_total(computer_cards):
            print(f"""You win!!
                 Your cards:{player_cards}          computer cards:{computer_cards}

                  Your score : {get_hand_total(player_cards)} and Computer score : {get_hand_total(computer_cards)}""")
            play_or_quit()
        elif get_hand_total(player_cards) < get_hand_total(computer_cards):
            print(f"""Computer wins!!  
                  Your cards:{player_cards}          computer cards:{computer_cards} 
                  Your score : {get_hand_total(player_cards)} and Computer score : {get_hand_total(computer_cards)}""")
            play_or_quit()
        elif get_hand_total(player_cards) == get_hand_total(computer_cards):
            print(f"""It's a tie!  
                  Your cards:{player_cards}          computer cards:{computer_cards} 
                  Your score : {get_hand_total(player_cards)} and Computer score : {get_hand_total(computer_cards)}""")


            play_or_quit()



wanna_play = input("Would you like to play the game of Black Jack? (y/n): ").lower()
if wanna_play == "y":
    print(logo)
    print("Welcome to the Black Jack!")
    card_picker()





else:
    print("Stop being a dih and play it bhai.Or nvm you gon miss out on ts.")

