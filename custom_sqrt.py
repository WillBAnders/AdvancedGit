import argparse
import math


def custom_sqrt(number):
    # TODO: implementation
    return math.sqrt(number)


parser = argparse.ArgumentParser(description="Calculate the square root of a number")
parser.add_argument("number", type=int)
args = parser.parse_args()

print(custom_sqrt(args.number))
