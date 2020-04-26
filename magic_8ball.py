"""
File: magic_8ball

"""
import random


def main():
    """

    """

    one_shake()

def one_shake():
    # Asks user for a yes or no question.
    user_input = input("Ask a yes or no question: ")
    # Checks to see if user enter a blank string, if so exits
    while user_input != "":
        # Generates random number.
        x = random.randint(1, 5)
        # Stores random number in a variable that has a statement attached.
        if x == 1:
            print("As I see it, yes")
        if x == 2:
            print("Ask again later.")
        if x == 3:
            print("Better not tell you now.")
        if x == 4:
            print("Cannot predict now.")
        if x == 5:
            print("Don't count on it")
        # Resets user input to allow while loop.
        user_input = input("Ask a yes or no question: ")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
