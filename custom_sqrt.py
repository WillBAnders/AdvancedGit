import argparse
import math


def custom_sqrt(number):
    if number < 0:
        return -math.sqrt(-number)
    return math.sqrt(number)


parser = argparse.ArgumentParser(description="Calculate the square root of a number")
parser.add_argument("number", type=float)
args = parser.parse_args()

print(custom_sqrt(args.number))
