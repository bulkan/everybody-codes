import itertools
import math


if __name__ == "__main__":
    with open("p2.txt", "r") as f:
        gears = [int(line) for line in f.read().split("\n") if len(line)]

        gear_speed = math.prod([(a / b) for a, b in itertools.pairwise(gears)])

        print("p2 - ", 10000000000000 / gear_speed)
