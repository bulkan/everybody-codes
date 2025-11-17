import itertools
import math


def main(test_input: str):
    gear_strs = test_input.split("\n")

    gear_strs.pop()

    first_gear = gear_strs.pop(0)
    last_gear = gear_strs.pop()

    gear_strs = itertools.chain.from_iterable([g.split("|") for g in gear_strs])

    gear_speed = math.prod(
        [
            (int(a) / int(b))
            for a, b in itertools.batched([first_gear, *gear_strs, last_gear], 2)
        ]
    )

    print(gear_speed * 100)


if __name__ == "__main__":
    with open("p3.txt", "r") as f:
        input = f.read()

        main(input)
