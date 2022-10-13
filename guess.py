#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: October 2022
# This program uses if statements to guess a random number
#    with user input

import constants


def main():
    # this uses if statements to guess a random number

    # input
    integer_one = int(input("Enter integer one: "))
    integer_two = int(input("Enter integer two: "))

    # process
    sum = integer_one + integer_two

    # output
    print("\nSum is {}.".format(sum))

    print("\nDone.")


if __name__ == "__main__":
    main()
