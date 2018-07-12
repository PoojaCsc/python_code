def main():
    while True:
        print("-------Menu--------")
        print("Enter A for Addition")
        print("Enter S for Substraction")
        print("Enter M for Multiplication")
        print("Enter D for Division")
        print("Enter Q to quit")
        user_input = input(">")
        user_input = user_input.upper()


        if user_input == 'A':
            num1=float(input("Enter 1st number:"))
            num2=float(input("Enter 2nd number:"))
            result = num1 + num2
            print("Result is ", result)

        elif user_input == 'S':
            num1=float(input("Enter 1st number:"))
            num2=float(input("Enter 2nd number:"))
            result = num1 - num2
            print("Result is ", result)

        elif user_input == 'M':
            num1=float(input("Enter 1st number:"))
            num2=float(input("Enter 2nd number:"))
            result = num1 * num2
            print("Result is ", result)

        elif user_input == 'D':
            num1=float(input("Enter 1st number:"))
            num2=float(input("Enter 2nd number:"))
            result = num1 / num2
            print("Result is ", result)

        elif user_input == 'Q':
            break

        else:
            print("Wrong input")

if __name__ == "__main__":
    main()
