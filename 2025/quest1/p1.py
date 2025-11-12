from dataclasses import dataclass
from typing import List, Tuple
from parsita.util import splat
from parsita import ParserContext, lit, reg, repsep


@dataclass(frozen=True)
class Notes:
    names: List[str]
    instructions: List[Tuple[str, int]]


class NotesParsers(ParserContext, whitespace=r"\s*"):
    names = repsep(reg(r"\w+"), ",")

    number = reg(r"\d+") > int
    instruction = lit("L", "R") & number > splat(lambda a, b: (a, b))
    instructions = repsep(instruction, ",")

    value = names & instructions > splat(Notes)


if __name__ == "__main__":
    with open("p1.txt", "r") as f:
        content = f.read()

        result = NotesParsers.value.parse(content).unwrap()

        print(result.names)

        c = 0

        for dir, amount in result.instructions:
            match dir:
                case "L":
                    c = max(0, c - amount - 1)
                case "R":
                    c = min(10, c + amount + 1)

            print(dir, amount, c)

        print(result.names[c])
