import itertools
from typing import Optional
from parser import parse
from pprint import pp


def solve(input: str) -> Optional[str]:
    notes = parse(input)

    rules = notes.rules

    valid = True
    for name in notes.names:
        valid = all([l in rules and r in rules[l] for l, r in itertools.pairwise(name)])  # noqa: E741

        if valid:
            pp(name)
            return name


def test1():
    input = """Uraketh,Oronris,Urakris,Oroneth,Uraketh

r > a,i,o
i > p,w
n > e,r
o > n,m
k > f,r
a > k
U > r
e > t
O > r
t > h"""

    assert solve(input) == "Oroneth"


def p1():
    with open("p1.txt", "r") as f:
        solve(f.read())


def main():
    test1()
    p1()


if __name__ == "__main__":
    main()
