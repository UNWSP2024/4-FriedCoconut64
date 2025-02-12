def main():

    global more_movies
    global Tickets
    Tickets = 0
    more_movies = True
    while more_movies == True:
        movie_name = (input("What movie would you like to see? "))
        new_tickets = int(input("How many tickets would you like?"))
        Tickets = Tickets + new_tickets
        if new_tickets <= 0:
            print("Error: Tickets cannot be negative or zero, please try again")
        else:
            prompt_again =  input("Would you like to see another movie? (type 'Y' for yes)")
            if prompt_again == 'Y':
                more_movies = True
            else:
                more_movies = False
                print("Total number of tickets:", Tickets)
                print("Thank you for your purchases")
                break
if __name__ == '__main__':
    main()

    # Program #2, Donovan Thompson 2/12/25
