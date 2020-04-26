"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    This program will take two real numbers for the user and subtract them. It will then print
    the value for the user.
    """
    subtract_two_numbers()

def subtract_two_numbers():
    print("This program subtracts one number from another")
    # Prompts user for first number
    num1 = float(input("Enter first number "))
    # Prompts user for second number
    num2 = float(input("Enter second number "))
    # Determines the answer
    total = num1 - num2
    print("The result is " + str(total))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
