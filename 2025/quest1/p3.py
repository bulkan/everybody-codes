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
    with open("p3.txt", "r") as f:
        content = f.read()

        result = NotesParsers.value.parse(content).unwrap()

        c = 0

        length = len(result.names)

        for dir, amount in result.instructions:
            prev_top = result.names[0]

            target = 0

            match dir:
                case "L":
                    target -= amount % length
                case "R":
                    target += amount % length

            result.names[0] = result.names[target]
            result.names[target] = prev_top

        print(result.names[0])
