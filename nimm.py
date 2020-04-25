"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    """

    """
    total_stones = 20
    players_turn = 1

    # This will run while the number of is greater than 0
    while total_stones > 1:
        # Prints the number of stones left and prompts which players turn it is
        if total_stones != 0:
            print("There are " + str(total_stones) + " stones left")
            if players_turn == 1:
                player_pick = int(input("player one, would you like to remove 1 or 2 stones? "))
                while player_pick != 1 and player_pick != 2:
                    player_pick = int(input("Please enter only 1 or 2: "))
                total_stones -= player_pick
                players_turn -= 1
            elif players_turn == 0:
                player_pick = int(input("Player two, would you like to remove 1 or 2 stones? "))
                while player_pick != 1 and player_pick != 2:
                    player_pick = int(input("Please enter only 1 or 2: "))
                total_stones -= player_pick
                players_turn += 1
    while total_stones == 1:
        print("There are " + str(total_stones) + " stones left")
        if players_turn == 1:
            player_pick = int(input("player one, would you like to remove 1? "))
            while player_pick != 1:
                player_pick = int(input("you can only take one stone: "))
            total_stones -= player_pick
            players_turn -= 1
        elif players_turn == 0:
            player_pick = int(input("Player two, would you like to remove 1? "))
            while player_pick != 1:
                player_pick = int(input("You can only take one stone: "))
            total_stones -= player_pick
            players_turn += 1
    # If the number of stones is 0 this prints game over and which player won the game
    if total_stones == 0:
        if players_turn == 1:
            print("Game Over! Player one wins! ")
        elif players_turn == 0:
            print("Game Over! Player two wins! ")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
