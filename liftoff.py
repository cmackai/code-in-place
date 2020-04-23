"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    This program uses a for loop to count down a rocket launch. It uses a
    variable to store the number in the count down and subtract one from it
    as the program loops.
    """
    num1 = 10
    for i in range(10):
        print(num1)
        num1 -= 1
    print("Liftoff!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
