from dataclasses import dataclass
from parsita import ParserContext, repsep, rep, reg


@dataclass(frozen=True)
class Notes:
    names: list[str]
    rules: dict[str, set[str]]


class NotesParsers(ParserContext, whitespace=r"[ \t]*"):
    names = repsep(reg(r"\w+"), ",") << "\n" << "\n"

    newline = reg(r"(\n)?")
    rule = reg(r".") & ">" >> repsep(reg(r"."), ",") << newline
    rules = rep(rule)

    values = names & rules


def parse(input: str) -> Notes:
    names, rules_list = NotesParsers.values.parse(input).unwrap()

    rules = {left: set(after) for left, after in rules_list}

    return Notes(names=names, rules=rules)
