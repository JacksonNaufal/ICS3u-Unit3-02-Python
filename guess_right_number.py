#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a guess the random number program

import constants


def main():

    # This is a random number guesser

    # input
    random_number = int(input("Enter your first guess here (0-9): "))

    # process & output
    if random_number != constants.guess_number:
        print("Guess is incorrect")
    if random_number == constants.guess_number:
        print("Guess is correct!")


if __name__ == "__main__":
    main()
