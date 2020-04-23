"""
File: moon_weight.py
--------------------
Add your comments here.
"""
MOON_CONSTANT = .165

def main():
    """
    This program will take the weight of the user as an input and convert it
    to what their weight would be on the Moon.
    """
    earthweight = float(input("Enter a weight on earth in lbs. "))
    moonweight = earthweight * MOON_CONSTANT
    print("Your equivalent weight on the Moon is " + str(moonweight) + " lbs.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
