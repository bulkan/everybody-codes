# knight_mentor = []
#
# iterate through swordests
# when A is seen add its position knight_mentor
# when a is seen check if knight_mentor if there is a positio < a


def parse(input: str) -> list[str]:
    swordests = [c for c in input if c in "Aa"]

    return swordests
