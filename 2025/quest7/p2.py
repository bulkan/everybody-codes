import itertools
from parser import parse
from pprint import pp


def solve(input: str) -> int:
    notes = parse(input)

    rules = notes.rules

    valid_name_indices: list[int] = []
    for index, name in enumerate(notes.names, 1):
        valid = all([l in rules and r in rules[l] for l, r in itertools.pairwise(name)])  # noqa: E741

        if valid:
            valid_name_indices.append(index)

    res = sum(valid_name_indices)
    pp(res)
    return res


def test1():
    input = """Xanverax,Khargyth,Nexzeth,Helther,Braerex,Tirgryph,Kharverax

r > v,e,a,g,y
a > e,v,x,r
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i"""

    assert solve(input) == 23


def p2():
    with open("p2.txt", "r") as f:
        solve(f.read())


def main():
    test1()
    p2()


if __name__ == "__main__":
    main()
