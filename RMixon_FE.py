def main():
    firstName = str(input("Please enter your First Name: "))
    lastName = str(input("Please enter your Last Name: "))
    ageInYears = float(input("Please enter your age in years: "))
    ageInMonths = float(ageInYears * 12)
    ageInDays = float(ageInYears * 365)
    ageInHours = float(ageInDays * 24)
    ageInMinutes = float(ageInHours * 60)
    ageInSeconds = float(ageInMinutes * 60)

    print("")
    print(lastName + ', ' + firstName)
    print(ageInYears, 'years old')
    print(ageInMonths, 'months old')
    print(ageInDays, 'days old')
    print(ageInHours, 'hours old')
    print(ageInMinutes, 'minutes old')
    print(ageInSeconds, 'seconds old')


# calling the main function
main()
