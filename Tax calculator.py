""" Anil wants to calculate teh tax to be paid on his earnings. He doesn't remember the amount charged on the earnings. So he decided to create a program in python with functions to calculate the tax to be paid on his earnings. he collected the information and started creating the program and now he is happy to use the calcuator. Create the same kind of program so that you can use it in the future. """

def calculate_tax(earnings):
    """
    Calculate tax to be paid based on earnings.
    
    Args:
    - earnings: float, total earnings
    
    Returns:
    - float, tax amount to be paid
    """
    tax_brackets = [
        (10000, 0.10),
        (30000, 0.20),
        (70000, 0.30),
        (float('inf'), 0.40)
    ]
    
    remaining_earnings = earnings
    total_tax = 0
    
    for bracket in tax_brackets:
        bracket_limit, tax_rate = bracket
        if remaining_earnings <= 0:
            break
        elif remaining_earnings <= bracket_limit:
            total_tax += remaining_earnings * tax_rate
            break
        else:
            total_tax += bracket_limit * tax_rate
            remaining_earnings -= bracket_limit
    
    return total_tax

def main():

    print("****** WELCOME TO YOUR TAX CHECKER CALCULATOR ****** ")
    earnings = float(input("Enter your earnings: "))
    
    tax = calculate_tax(earnings)
    print(f"The tax to be paid on earnings of {earnings} is {tax}")

if __name__ == "__main__":
    main()
