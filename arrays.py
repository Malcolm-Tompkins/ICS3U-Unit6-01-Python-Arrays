#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on June 3, 2021
# Generates 3 random numbers from 1 and 100

import random


def main():
    random_numbers = []
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    number3 = random.randint(1, 100)
    number4 = random.randint(1, 100)
    number5 = random.randint(1, 100)
    random_numbers.append(number1)
    random_numbers.append(number2)
    random_numbers.append(number3)
    random_numbers.append(number4)
    random_numbers.append(number5)
    average_number = sum(random_numbers) / len(random_numbers)
    print("Your random numbers are: {}".format(random_numbers))
    print("The average of these numbers is: {}".format(average_number))
    print("Done.")


if __name__ == "__main__":
    main()
