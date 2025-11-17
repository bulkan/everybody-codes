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


def main(test_input: str):
    nums = [int(s) for s in test_input.split(":")[1:][0].split(",")]

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

    quality = "".join([str(segment.spine) for segment in segments])
    print(quality)

    # num = nums.pop(0)
    # root = current_segment = Segment(spine=num)
    # next_segment = None
    #
    # num = nums.pop(0)
    #
    # while num is not None:
    #     # wont be true for first iteration
    #     if current_segment.all_slots_filled():
    #         next_segment = Segment(spine=num)
    #         current_segment.next_segment = next_segment
    #         current_segment = next_segment
    #
    #     if num < current_segment.spine and current_segment.left is None:
    #         current_segment.left = num
    #         num = None
    #     elif num > current_segment.spine and current_segment.right is None:
    #         current_segment.right = num
    #         num = None
    #     elif next_segment:
    #         current_segment = next_segment
    #         next_segment = None
    #
    #     if not num and nums:
    #         num = nums.pop(0)

    # current = root
    # while current:
    #     print(current.left, current.spine, current.right)
    #
    #     current = current.next_segment


if __name__ == "__main__":
    # test_input = "58:5,3,7,8,9,10,4,5,7,8,8"

    with open("p1.txt", "r") as f:
        main(f.read())
