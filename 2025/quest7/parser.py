from dataclasses import dataclass
from parsita import ParserContext, repsep, reg


@dataclass(frozen=True)
class Notes:
    names: list[str]
    rules: dict[str, set[str]]


class NotesParsers(ParserContext, whitespace=r"[ ]*"):
    names = repsep(reg(r"\w+"), ",")

    rule = reg(r".") & ">" >> repsep(reg(r".*"), ",")
    rules = repsep(rule, "\n")

    values = names << "\n" << "\n" & rules


def parse(input: str) -> Notes:
    names, rules_list = NotesParsers.values.parse(input).unwrap()

    rules = {left: set(after) for left, after in rules_list}

    return Notes(names=names, rules=rules)
