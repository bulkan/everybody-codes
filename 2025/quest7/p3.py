import itertools
import pprint
from parser import parse
from pprint import pp


# for name in names
# start from last letter in name
#     if last_letter in rules append letter to name
#         is name >= min_letters  and <= max_letters
#               append to valid_names
#         if name >= max_letters; break


def solve(input: str) -> int:
    min_letter = 7
    max_letters = 11

    notes = parse(input)

    rules = notes.rules
    # pp(rules)

    valid_names: list[str] = []
    for index, name in enumerate(notes.names, 1):
        if name[-1] not in rules:
            continue

        letters_to_check = list(rules[name[-1]])
        # seen_letters = set()

        new_name = name

        while len(letters_to_check):
            ll = letters_to_check.pop()

            # if ll in seen_letters:
            #     continue

            if ll in rules:
                letters_to_check.extend(list(rules[ll]))

                new_name += ll

                new_length = len(new_name)

                if new_length >= min_letter and new_length <= max_letters:
                    pp(new_name)
                    valid_names.append(new_name)

            # seen_letters.add(ll)
    pp(valid_names)
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
    # p3()


if __name__ == "__main__":
    main()
