def main():
    x = 0
    month_count = 0
    year_rain = 0
    rain = 0
    months = (("January","Febuary","March","April","May","June","July","August","September","October","November","December"))
    years = int(input("How many years would you like to record?"))
    while years <= 0:
        print("Error: Must be above zero")
        years = int(input("Please try again:"))
    while x < years:
        for char in months:
            print(char)
            rain = float(input("How much did it rain in inches this month?"))
            year_rain += rain
            month_count += 1
        x += 1

    print("Total amount of months:", month_count)
    print("Total amount of rainfall:",year_rain)
    print("Average rain per month:", year_rain/month_count)



if __name__ == '__main__':
    main()
    
#Program #3, Donovan Thompson 2/12/25
