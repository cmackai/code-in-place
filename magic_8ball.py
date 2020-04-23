"""
File: magic_8ball

"""
import random


def main():
    """

    """
    one_shake()

def one_shake():
    user_input = input("Ask a yes or no question: ")
    while user_input != "":
        x = random.randint(1, 5)
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
    user_input == ""


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
