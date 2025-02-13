def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    more_purchases = True
    budget = float(input("How much have you budgeted for the month?:"))
    while budget < 0.0:
        budget = float(input("Error: Budget cannot be negative, please try again:"))
    while more_purchases == True:
        spent = float(input("How much did you spend?:"))
        total += spent
        x = input("Did you spend on anything else (type Y for yes)?:")
        if x == "Y":
            more_purchases = True
        else:
            more_purchases = False
    difference = budget - total
    print("Your Budget was:", budget)
    print("You spent:", total)
    if difference < 0:
        print("You have gone overbudget by:", difference)
    else:
        print("You are underbudget by:", difference)


if __name__ == '__main__':
    main()
    
#Program #5, Donovan Thompson 2/12/25
