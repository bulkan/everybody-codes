import itertools
from pprint import pp
from parser import parse


def solve(input: str) -> int:
    min_letters = 7
    max_letters = 11

    notes = parse(input)

    rules = notes.rules

    valid_names = set()

    def check_prefix(prefix: str) -> bool:
        return all(
            [l in rules and r in rules[l] for l, r in itertools.pairwise(prefix)]  # noqa: E741
        )

    def visit(current: str) -> None:
        if min_letters <= len(current) <= max_letters:
            valid_names.add(current)

        if len(current) > max_letters:
            return

        last_letter = current[-1]
        if last_letter not in rules:
            return

        for v in rules[last_letter]:
            visit(current + v)

    for name in notes.names:
        if check_prefix(name):
            visit(name)

    pp(len(valid_names))
    return len(valid_names)


def test1():
    input = """Xaryt

X > a,o
a > r,t
r > y,e,a
h > a,e,v
t > h
v > e
y > p,t"""

    assert solve(input) == 25


def p3():
    with open("p3.txt", "r") as f:
        solve(f.read())


def main():
    test1()
    p3()


if __name__ == "__main__":
    main()
