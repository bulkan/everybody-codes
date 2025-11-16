def multiply(a, b):
    [x1, y1] = a
    [x2, y2] = b

    return [x1 * x2 - y1 * y2, x1 * y2 + y1 * x2]


def add(a, b):
    [x1, y1] = a
    [x2, y2] = b
    return [x1 + x2, y1 + y2]


def divide(a, b):
    [x1, y1] = a
    [x2, y2] = b
    return [int(x1 / x2), int(y1 / y2)]


if __name__ == "__main__":
    """
    Multiply the result by itself.
    Divide the result by  [10,10].
    Add  A  to the result.
    """

    res = [0, 0]

    # A = [25, 9]
    A = [153, 56]

    for i in range(3):
        print(i)
        res = multiply(res, res)
        res = divide(res, [10, 10])
        res = add(res, A)

    print(res)
