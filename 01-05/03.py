import re
from collections import Counter

PATTERN = re.compile('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')


def match(line):
    id_, left_, top_, width_, height_ = re.match(PATTERN, line).groups()
    return id_, int(left_), int(top_), int(width_), int(height_)


with open("03_input.txt") as input_file:
    input_ = [line.strip() for line in input_file.readlines()]
    points = {}

    for line in input_:
        claim_id, left, top, width, height = match(line)
        points[claim_id] = [(x, y) for x in range(left, left + width) for y in range(top, top + height)]

    counts = Counter([point for claim_points in points.values() for point in claim_points])

    # part 1
    print(sum(n > 1 for n in counts.values()))

    # part 2
    print(next(claim_id
               for claim_id, claim_points in points.items()
               if all(counts.get(claim_point) == 1 for claim_point in claim_points)))
