from pprint import pp
from parser import parse


def p1_pairs(input: str):
    swordists = parse(input)

    knight_mentors = []

    pairs = 0

    for i, c in enumerate(swordists):
        match c:
            case "A":
                knight_mentors.append(i)
            case "a":
                pairs += len([p for p in knight_mentors if p <= i])

    pp(pairs)


def p1():
    with open("p1.txt", "r") as f:
        p1_pairs(f.read())


def test1():
    test_input = "ABabACacBCbca"
    p1_pairs(test_input)


def main():
    test1()
    p1()


if __name__ == "__main__":
    main()
