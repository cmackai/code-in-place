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

    while total_stones != 0:
        if total_stones != 0:
            print("There are " + str(total_stones) + " stones left")
            if players_turn == 1:
                player_pick = int(input("player one, would you like to remove 1 or 2 stones? "))
                total_stones -= player_pick
                players_turn -= 1
            elif players_turn == 0:
                player_pick = int(input("Player two, would you like to remove 1 or 2 stones? "))
                total_stones -= player_pick
                players_turn += 1
    if total_stones == 0:
        if players_turn == 1:
            print("Game Over! Player one wins! ")
        elif players_turn == 0:
            print("Game Over! Player two wins! ")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
