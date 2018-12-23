import itertools
from collections import defaultdict, deque

PLAYER_COUNT = 423
MARBLE_COUNT = 7194400  # divide by 100 for part 1

marbles = deque([0])
scores = defaultdict(int)
players = itertools.cycle(list(range(1, PLAYER_COUNT + 1)))
player = next(players)

for marble in range(1, MARBLE_COUNT + 1):
    player = next(players)
    if not marble % 23:
        marbles.rotate(-7)
        scores[player] += marble + marbles.pop()
        continue
    marbles.rotate(2)
    marbles.append(marble)

print(max(scores.values()))
