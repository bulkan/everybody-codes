from dataclasses import dataclass


# knight_mentor = []
#
# iterate through swordests
# when A is seen add its position knight_mentor
# when a is seen check if knight_mentor if there is a positio < a


@dataclass()
class Professions:
    fencers: list[str]
    archers: list[str]
    magicians: list[str]


def parse(input: str) -> Professions:
    fencers = [c for c in input if c in "Aa"]
    archers = [c for c in input if c in "Bb"]
    magicians = [c for c in input if c in "Cc"]

    return Professions(fencers, archers, magicians)
