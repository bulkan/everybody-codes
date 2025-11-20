from parsita import ParserContext, repsep, reg
from pprint import pp


class NotesParsers(ParserContext, whitespace=r"[ ]*"):
    names = repsep(reg(r"\w+"), ",")

    rule = reg(r".") & ">" >> repsep(reg(r".*"), ",")
    rules = repsep(rule, "\n")

    values = names << "\n" << "\n" & rules


def parse(input: str):
    names = NotesParsers.values.parse(input).unwrap()

    pp(names)
