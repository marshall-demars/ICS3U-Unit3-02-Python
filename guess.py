#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: October 2022
# This program uses if statements to guess a random number
#    with user input

import constants


def main():
    # this uses if statements to guess a random number

    # input
    random_number = int(input("Enter a number between 1 and 9: "))

    # process and output
    if random_number == constants.CHOSEN_NUMBER:
        print("You guessed correctly!")
    if random_number != constants.CHOSEN_NUMBER:
        print("You guessed incorrectly.")

    print("\nDone.")


if __name__ == "__main__":
    main()
