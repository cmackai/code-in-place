"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MIN_RANDOM = 0
MAX_RANDOM = 100

def main():
    """
    This program will print a addition problem for the user to answer.
    """
    addition_problem()


def addition_problem():

    count = 1

    while count != 4:
        # Generates two random numbers for the user to add.
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        # Asks the user for the answer as input.
        user_num = input("What is " + str(num1) + " + " + str(num2) + " ? ")
        # Finds the answer to the addition question
        total = num1 + num2
        # Checks if the user entered the right answer.
        if int(user_num) == total:
            # Prints statement while user is getting correct answers
            print("Correct! You've gotten " + str(count) + " correct in a row ")
            count += 1
        else:
            # Prints statement while user is not getting correct answer
            print("Incorrect, the correct answer was " + str(total) + " please try again! ")
    # Once user has three correct answers in a row, prints message and ends program
    else:
        print("Congrats! You have mastered addition!")

#def check_answer():


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
