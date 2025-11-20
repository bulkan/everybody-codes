from collections import defaultdict
from pprint import pp
from tqdm import tqdm


def solve(input: str, repeat: int, distance: int) -> int:
    # probably dont need to actually repeat the string
    # but can math our way... but here we are
    # tents = input * repeat
    #
    # mentors_pos = defaultdict(set)
    #
    # for i, c in tqdm(enumerate(tents), desc="calculating mentors_pos"):
    #     if c in {"A", "B", "C"}:
    #         mentors_pos[c.lower()].add(i)
    #
    # count = 0
    #
    # for i, c in tqdm(enumerate(tents), desc="counting"):
    #     if c not in {"a", "b", "c"}:
    #         continue
    #
    #     start = max(i - limit, 0)
    #     stop = min(i + limit, len(tents) - 1)
    #
    #     for i in range(start, stop + 1):
    #         if i in mentors_pos[c]:
    #             count += 1

    res = 0
    for letter in ["a", "b", "c"]:
        novices = [int(c == letter) for c in input] * repeat
        mentors = [int(c == letter.upper()) for c in input] * repeat
        for i, m in tqdm(enumerate(mentors)):
            if m == 1:
                lb = max(0, i - distance)
                ub = min(i + 1 + distance, len(novices))
                res += sum(novices[lb:ub])

    # pp(mentors_pos)
    pp(res)
    return res


def test1():
    input = "AABCBABCABCabcabcABCCBAACBCa"
    assert solve(input, repeat=1, distance=10) == 34
    assert solve(input, repeat=2, distance=10) == 72
    assert solve(input, repeat=1000, distance=1000) == 3442321


def p3():
    with open("p3.txt", "r") as f:
        solve(f.read(), repeat=1000, distance=1000)


def main():
    test1()
    p3()


if __name__ == "__main__":
    main()
