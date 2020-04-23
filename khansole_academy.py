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


# This prompts the user with the problem and takes their input
def addition_problem():

    count = 1

    while count != 4:
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        user_num = input("What is " + str(num1) + " + " + str(num2) + " ? ")
        total = num1 + num2
        if int(user_num) == total:
            print("Correct! You've gotten " + str(count) + " correct in a row ")
            count += 1
        else:
            print("Incorrect, the correct answer was " + str(total) + " please try again! ")
    else:
        print("Congrats! You have mastered addition!")

#def check_answer():


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
