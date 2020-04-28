"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    This program will run through the hailstone math puzzle, when a user enters an integer.
    """

    n = int(input("Enter a positive integer: "))
    while n != 1:
        if n % 2 == 0:
            n2 = n / 2
            print(str(n) + " is even, so I take half: " + str(n2))
            n = n / 2
        else:
            n2 = (n * 3) + 1
            print(str(n) + " is odd, so I make 3n+1: " + str(n2))
            n = (n * 3) + 1

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
