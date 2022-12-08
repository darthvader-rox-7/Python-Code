def factorial_1():
    number = int(input("Choose a number to get its factorial: "))
    factorial1 = 1
    n = 1
    while n != number + 1:
        factorial1 = factorial1*n
        n += 1

    else: 
        print(factorial1)
    universe()

def factorial_2():

    limit = int(input("To what number do you want to get your list of factorials? "))

    factorial2 = 1

    for i in range(1, limit + 1):
        factorial2 = factorial2 * i
        print(factorial2)
        i += 1
    universe()

def universe():
    print("Choose your command:")
    print("1) Get the factorial of a number.")
    print("2) Get a list of factorials.")
    print("3) Stop the program.")
    choice = int(input("Your Option (1/2/3): "))

    if choice == 1:
        factorial_1()

    elif choice == 2:
        factorial_2()

    elif choice == 3:
        validity = input("Are you sure you want to exit? (Y/N) ")
        validity.upper()
        if validity == "Y":
            exit()

        elif validity == "N":
            universe()

        else:
            "Please choose a valid option."
            universe()

    else:
        "Please choose a valid option."
        universe()

universe()