"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

def main():
    """
    This program will print a list of 10 integers from 0 - 100
    """
    # Prints an amount of random numbers from a predetermined range
    # This can be changed using the constants above
    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM, MAX_RANDOM))




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
