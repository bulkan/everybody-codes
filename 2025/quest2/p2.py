import itertools
from typing import Tuple


def multiply(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    x1, y1 = a
    x2, y2 = b

    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)


def add(a: Tuple[int, int], b: Tuple[int, int]):
    x1, y1 = a
    x2, y2 = b
    return (x1 + x2, y1 + y2)


def divide(a: Tuple[int, int], b: Tuple[int, int]):
    x1, y1 = a
    x2, y2 = b
    return (int(x1 / x2), int(y1 / y2))


if __name__ == "__main__":
    count = 0
    [Ax, Ay] = [-21703, -68997]
    for xd, yd in itertools.product(range(1001), range(1001)):
        # P = add(A, [10 * xd, 10 * yd])

        P = (Ax + xd, Ay + yd)

        result = (0, 0)
        valid = True

        for _ in range(100):
            result = multiply(result, result)
            result = divide(result, (100000, 100000))
            result = add(result, P)
            if any(abs(num) > 1000000 for num in result):
                valid = False
                break
        if valid:
            count += 1
    print(count)
