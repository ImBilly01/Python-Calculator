def main():

    choice = input("A/a = Addition\n S/s = Subtraction\n M/m = Multiplication\n D/d = Division\n P/p = Power\n N/n = Negation\n R/r = Reminder\n Select an option: ")
    print(" ")
    num = input("First Number: ")
    print(" ")
    num1 = input("Second Number: ")
    print(" ")


    def addition(first, second):
        total = int(num) + int(num1)
        print(total)
        print(" ")

    def subtraction(first, second):
        total = int(num) - int(num1)
        print(total)
        print(" ")

    def multiplication(first, second):
        total = int(num) * int(num1)
        print(total)
        print(" ")

    def division(first, second):
        total = float(num) / float(num1)
        print(total)
        print(" ")

    def power(first, second):
        total = int(num) ** int(num1)
        print(total)
        print(" ")

    def negation(first):
        total = float(num)
        print(-total)

    def remainder(first, second):
        total = float(num) % float(num1)
        print(total)

    if choice == "A":
        addition(first = num, second = num1)

    elif choice == "a":
        addition(first = num, second = num1)

    elif choice == "S":
        subtraction(first = num, second = num1)

    elif choice == "s":
        subtraction(first = num, second = num1)

    elif choice == "M":
        multiplication(first = num, second = num1)

    elif choice == "m":
        multiplication(first = num, second = num1)

    elif choice == "D":
        division(first = num, second = num1)

    elif choice == "d":
        division(first = num, second = num1)

    elif choice == "P":
        power(first = num, second = num1)

    elif choice == "p":
        power(first = num, second = num1)

    elif choice == "N":
        negation(first = num)

    elif choice == "n":
        negation(first = num)

    elif choice == "R":
        remainder(first = num, second = num1)

    elif choice == "r":
        remainder(first = num, second = num1)

    else:
        print("It's probably because you didn't select any option or you wrote something wrong.")
        print(" ")

    # closeInput = input("Press ENTER to exit")
    # print("Closing...")

    restart = input("Would you like to restart? (yes/no) ")
    if restart == "yes":
        main()
    elif restart == "no":
        print(" ")
        closeInput = input("Press ENTER to exit")
        print("Closing...")
main()