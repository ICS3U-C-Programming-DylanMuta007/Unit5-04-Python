#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : May 2025
# This program is a calculates the result of two value/number using the given operator


# function definition for calc()
def calc(user_sign, num1, num2):
    # checks for what sign is given and does a math operation depending on the sign
    if user_sign == "+":
        return num1 + num2
    elif user_sign == "-":
        return num1 - num2
    elif user_sign == "/":
        return num1 / num2
    elif user_sign == "*":
        return num1 * num2
    elif user_sign == "%":
        return num1 % num2


def main():

    # Getting the sign, and numbers from user
    user_sign = input("What is the operator will you be using (+, -, /, *, %): ")
    numb1_string = input("What is the first number you will be using: ")
    numb2_string = input("What is the second number you will be using: ")

    # Concerting given input into float (except for sign)
    try:
        num1 = float(numb1_string)
        try:
            numb2 = float(numb2_string)

            # Checks if user gave all appropriate signs
            if (
                user_sign == "+"
                or user_sign == "-"
                or user_sign == "/"
                or user_sign == "*"
                or user_sign == "%"
            ):
                # If the second number is 0 and sign is % or ? says that its invalid
                if user_sign == "/" or user_sign == "%":
                    if numb2 == 0:
                        print("Division by 0 isn't allowed")

                    # If it is division but the second number isn't 0 then runs operation
                    else:
                        print("")
                        result = calc(user_sign, num1, numb2)
                        print(f"{num1} {user_sign} {numb2} = {result}")

                # If it wasn't / or % then runs the operation
                else:
                    print("")

                    # Function call
                    result = calc(user_sign, num1, numb2)
                    print(f"{num1} {user_sign} {numb2} = {result}")

            else:
                print(f"{user_sign} is not a valid operand")
        # Checks for any error with the second number
        except ValueError:
            print(f"{numb2_string} is not a number")

    # Checks for any error with the First number
    except ValueError:
        print(f"{numb1_string} is not an number")


if __name__ == "__main__":
    main()
