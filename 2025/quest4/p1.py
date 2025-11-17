import itertools
import math


if __name__ == "__main__":
    with open("p1.txt", "r") as f:
        gears = [int(line) for line in f.read().split("\n") if len(line)]

        gear_speed = math.prod([(a / b) for a, b in itertools.pairwise(gears)])

        print("p1 - ", int(gear_speed * 2025))
        print("p2 - ", gear_speed, 10000000000000 / gear_speed)
