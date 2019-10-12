"""
USING "DEF" FUNCTION TO APPLY PARAMETERS
TO CREATE..
A CALCULATOR
"""

def SMCALC():
    loc1 = float(input("Enter value one:"))
    OP = input("Enter Operation: ")
    loc2 = float(input("Enter value two:"))

    """
       Using "if" loops, you have to make sure the loop ends,
       with an "else" loop.
    """
    if OP == "+":
        print(loc1 + loc2)
    elif OP == "-":
        print(loc1 - loc2)
    elif OP == "*":
        print(loc1 * loc2)
    elif OP == "/":
        print(loc1 / loc2)
    else:
        print("INPUT ERROR!!")

print(SMCALC())






