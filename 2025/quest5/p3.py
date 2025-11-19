import pprint
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass()
class Segment:
    spine: int
    left: Optional[int] = None
    right: Optional[int] = None

    def level(self) -> int:
        level = "".join(
            [str(n) for n in [self.left, self.spine, self.right] if n is not None]
        )
        return int(level)

    def all_slots_filled(self) -> bool:
        return self.left is not None and self.right is not None

    def __str__(self) -> str:
        return f"{self.left}-{self.spine}-{self.right}"


@dataclass()
class Sword:
    id: int
    quality: int
    segments: List[Segment]

    def segments_to_string(self) -> str:
        return ",".join([str(s.level()) for s in self.segments])

    def __str__(self) -> str:
        return f"{self.quality} - {self.id} - {self.segments_to_string()}"


swords: List[Sword] = []


def sword_compare(sword: Sword) -> Tuple[int, Tuple[int, ...], int]:
    levels = [s.level() for s in sword.segments]

    return (sword.quality, tuple(levels), sword.id)


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

        swords.append(
            Sword(
                id=int(id),
                quality=int("".join([str(segment.spine) for segment in segments])),
                segments=segments,
            )
        )

    # def sword_compare(a: Sword, b: Sword) -> int:
    #     if a.quality == b.quality:
    #         for seg_a, seg_b in zip(a.segments, b.segments):
    #             if seg_a.level() > seg_b.level():
    #                 return 1
    #
    #         if a.id > b.id:
    #             return -1
    #         if a.id < b.id:
    #             return 1
    #     if a.quality > b.quality:
    #         return -1
    #     if a.quality < b.quality:
    #         return 1
    #
    #     print("wtf2")
    #     return 0
    #
    # sorted_swords = sorted(swords, key=cmp_to_key(sword_compare))

    sorted_swords = sorted(swords, key=sword_compare, reverse=True)

    checksum = sum([sword.id * index for index, sword in enumerate(sorted_swords, 1)])

    pprint.pp(checksum)


if __name__ == "__main__":
    # test_input = """1:7,1,9,1,6,9,8,3,7,2
    #  2:6,1,9,2,9,8,8,4,3,1
    #  3:7,1,9,1,6,9,8,3,8,3
    #  4:6,1,9,2,8,8,8,4,3,1
    #  5:7,1,9,1,6,9,8,3,7,3
    #  6:6,1,9,2,8,8,8,4,3,5
    #  7:3,7,2,2,7,4,4,6,3,1
    #  8:3,7,2,2,7,4,4,6,3,7
    #  9:3,7,2,2,7,4,1,6,3,7"""
    #
    # #     test_input = """1:7,1,9,1,6,9,8,3,7,2
    # # 2:7,1,9,1,6,9,8,3,7,2"""
    # main(test_input)

    with open("p3.txt", "r") as f:
        main(f.read())
