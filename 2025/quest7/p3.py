from parser import parse
from pprint import pp


# for name in names
# start from last letter in name
#     if last_letter in rules append letter to name
#         is name >= min_letters  and <= max_letters
#               append to valid_names
#         if name >= max_letters; break


def solve(input: str) -> int:
    min_letters = 7
    max_letters = 11

    notes = parse(input)

    rules = notes.rules

    def recurser(name: str):
        if len(name) == max_letters:
            return {name}

        last_letter = name[-1]
        letters = rules.get(last_letter, None)

        if letters is None:
            return {name}

        new_names = [name + c for c in letters]
        return set.union({name}, *[recurser(n) for n in new_names])

    res = set()
    for _, name in enumerate(notes.names, 1):
        if name[-1] not in rules:
            continue

        for i in range(len(name) - 1):
            if name[i + 1] not in rules.get(name[i], set()):
                break
        else:
            res = res.union(recurser(name))

    res = len([r for r in res if len(r) >= min_letters])
    pp(res)
    return res


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
