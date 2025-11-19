from pprint import pp
from parser import parse


def p1_pairs(input: str):
    professions = parse(input)

    knight_mentors = []

    pairs = 0

    for i, c in enumerate(professions.fencers):
        match c:
            case "A":
                knight_mentors.append(i)
            case "a":
                pairs += len([p for p in knight_mentors if p <= i])

    pp(("p1_pairs", pairs))


def p2_pairs(input: str):
    professions = parse(input)

    pairs = 0

    for profession in [professions.fencers, professions.archers, professions.magicians]:
        mentors = []
        for i, c in enumerate(profession):
            match c:
                case "A" | "B" | "C":
                    mentors.append(i)
                case "a" | "b" | "c":
                    pairs += len([p for p in mentors if p <= i])

    pp(("p2_pairs", pairs))


def p1():
    with open("p1.txt", "r") as f:
        p1_pairs(f.read())


def p2():
    with open("p2.txt", "r") as f:
        p2_pairs(f.read())


def test1():
    test_input = "ABabACacBCbca"
    p1_pairs(test_input)
    p2_pairs(test_input)


def main():
    test1()
    p1()
    p2()


if __name__ == "__main__":
    main()
