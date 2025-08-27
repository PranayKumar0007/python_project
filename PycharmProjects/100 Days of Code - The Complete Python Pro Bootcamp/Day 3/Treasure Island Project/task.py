print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("""You walk forward into the dense woods and find a massive castle .
Exploring it might lead you to the treasure!
But make sure to stay alert!One wrong turn and your Life is out of your hands.\n""")

Task_1 = input("Which way would you like to choose? Left or Right?\n").lower()
if Task_1 == "left" :
    print("The SATANIC WATERS behold your eyes.")
    task_2 = input("Would you like to swim or wait?\n").lower()
    if task_2 == "wait":
        print("""That was a life-saving decision! The waters drained off and you are now ambushed by Three Majestic Doors !
        --There is a Red door covered in blood!
        --A Blue door which drains your energy just by looking at it!
        --A Yellow door that looks ordinary which might hold a promising gift or a soul seizing experience """)
        task_3 = input("Which door would you dare to open? Red, Blue or Yellow?\n").lower()
        if task_3 == "yellow":
            print("""*DRAMATIC BGM* 
            *BALAYYA MOVIE LEVEL ELEVATION*
            --YOU! ARE THE CHOOSEN ONE!! YOU GET TO ENJOY ALL THE RICHES OF THIS ISLAND!!!
            --YOU WIN!!!!!!!!""")
        elif task_3 == "red":
            print("""Your fate made you enter the Red door which presented you to THE HUNGRY DRAGON!
            --You are now being eaten alive piece by piece.
            --The seductive drool of the dragon allows you to neither pass out nor die of pain
            --Your voice screeches the entire room echoing louder and louder while the dragon rips you apart 
                  *****GAME OVER***** """)

        else:
            print("""Your lame ass was exposed to the outer space , You float around for several weeks in the vast space and find no life .ATP you are just waiting to die.
                  --Then you see a sparkling light which might be from a rescue spaceship and you fill your dumass heart with hope.
                  --Just to realise that you are now being engulfed by a black hole.
                  --Your body is being expanded and contracted just within the limits of elasticity so that you dont get ripped apart but feel the ends of hell
                  --*****GAME OVER***** """)
    else:
        print("""How dumb can a person be to swim across THE SATANIC WATERS?
        --Your dumass deserves to die.
        --Can't believe a biggot like you tried to play this game and win the treasure
        --Congrats you die at the the second challenge of the game.
        --Imagine how lame it is to die at this dumb fuckin text game in the second challenge.
              ***GAME OVER***""")
else:
    print("""Can you believe this?
    --You just fucking lost .
    --C'mon bhai this was the first challenge.
    --I bet your family hates you for being a useless piece of shit
          ***GAME OVER***""")

    ### learnings : - Use .lower() to make the if function work properly as the input gets all lowercased .
    ###             - \n makes the input answer go a line below which is just good for the aesthetics