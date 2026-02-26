import random



pele = {
    4 : 14 ,
    9 : 31 ,
    21 : 42 ,
    28 : 84 ,
    51 : 67 ,
    72 : 91 ,
    80 : 99 ,
}

mar = {
    17 : 7 ,
    62 :18 ,
    54 :34 ,
    64 :60 ,
    87 :36 ,
    93 :73 ,
    95 :75 ,
    98 :79
}

def print_welcome():
    print()
    print("=========================================================")
    print("Welcome to the game of Marpele!")
    print("Player 1 and Player 2 start at position 1.")
    print("First player to reach position 100 wins!")
    print("Roll the dice to move forward.")
    print("Good luck!\n")
    print("=========================================================")
    print()

def print_ladder_snake():
    print("Ladders:")
    print()
    for start, end in pele.items():
        print(f"  {start} -> {end}")
        print()
    print("Snakes:")
    print()
    for start, end in mar.items():
        print(f"  {start} -> {end}")
        print()
    print("=========================================================")


def roll_dice():
    global player_1, player_2, turn
    move = random.randint(1, 6)
    print(f" your dice shows : {move}")
    print()
    if turn % 2 == 0:
        if player_1 + move > 100:
            print(f"Move would exceed 100! Player 1 stays at position {player_1}")
            print("==========================================================")
            print()
            
        else:
            player_1 += move
            print(f"Player 1 is at position {player_1}")
            print()
            if player_1 in pele:
                player_1 = pele[player_1]
                print(f"Player 1 climbed a ladder to position {player_1}!")
                print()
                print(f"Player 1 is at position {player_1}")
                print()
            elif player_1 in mar:
                player_1 = mar[player_1]
                print(f"Player 1 slid down a snake to position {player_1}!")
                print()
                print(f"Player 1 is at position {player_1}")
                print()
        print("==========================================================")
    else:
        if player_2 + move > 100:
            print(f"Move would exceed 100! Player 2 stays at position {player_2}")
            print("==========================================================")
            print()
            
        else:
            player_2 += move
            print(f"Player 2 is at position {player_2}")
            print()
            if player_2 in pele:
                player_2 = pele[player_2]
                print(f"Player 2 climbed a ladder to position {player_2}!")
                print()
                print(f"Player 2 is at position {player_2}")
                print()
            elif player_2 in mar:
                player_2 = mar[player_2]
                print(f"Player 2 slid down a snake to position {player_2}!")
                print()
                print(f"Player 2 is at position {player_2}")
                print()
        print("==========================================================")

    if move == 6:
        print("Rolled a 6! Extra turn!")
        print("==========================================================")
        print()
        turn += 2  
    else:
        turn += 1
            

def print_positions():
    if turn % 2 == 0:
        print("player 1 turn : ")
        print(f"Player 1 is at position {player_1}")
        input("Press Enter to roll the dice...")
        roll_dice()
    else:
        print("player 2 turn : ")
        print(f"Player 2 is at position {player_2}")
        input("Press Enter to roll the dice...")
        roll_dice()






player_1 = 1
player_2 = 1
turn = 0

print_welcome()
print_ladder_snake()
while player_1 < 100 and player_2 < 100:
    print_positions()

if player_1 == 100:
    print()
    print("Player 1 wins!")
elif player_2 == 100:
    print()
    print("Player 2 wins!")