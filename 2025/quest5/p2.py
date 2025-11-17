from dataclasses import dataclass
from typing import Optional


@dataclass()
class Segment:
    spine: int
    left: Optional[int] = None
    right: Optional[int] = None

    def all_slots_filled(self) -> bool:
        return self.left is not None and self.right is not None

    def __str__(self) -> str:
        return f"{self.left}-{self.spine}-{self.right}"


swords = {}


def main(test_input: str):
    for line in test_input.split("\n"):
        if not line:
            break
        id, line = line.split(":")

        nums = [int(s) for s in line.split(",")]

        segments = [Segment(spine=nums.pop(0))]

        for num in nums:
            placed = False
            for segment in segments[:]:
                if segment.all_slots_filled():
                    continue

                if num < segment.spine and segment.left is None:
                    segment.left = num
                    placed = True
                elif num > segment.spine and segment.right is None:
                    segment.right = num
                    placed = True

                if placed:
                    break

            if not placed:
                segments.append(Segment(spine=num))

        swords[id] = int("".join([str(segment.spine) for segment in segments]))
    vals = sorted(swords.values())
    print(max(vals) - min(vals))


if __name__ == "__main__":
    with open("p2.txt", "r") as f:
        main(f.read())
