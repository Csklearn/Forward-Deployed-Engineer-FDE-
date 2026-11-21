import addition
from multiplcation import multiplication
from subtraction import subtraction
import userDetails.userdetails as ud

def main():
    addition.addition(2,3)
    multiplication(2,3)
    subtraction(2,3)
    addition.add_large_number(363737,383838)
    ud.userDetails()
    ud.userSummary()
    
if __name__ == "__main__": ## guard method
    main()