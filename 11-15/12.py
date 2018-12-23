YES = '#'
NO = '.'

GENERATIONS = 200  # replace with '20' for part 1

initial_state = '#.#..#.##.#..#.#..##.######...####.........#..##...####.#.###......#.#.##..#.#.###.#..#.#.####....##'

notes = [
    '.#### => .', '.###. => .', '#.... => .', '##### => .', '..### => #', '####. => #', '..#.. => .', '###.# => .',
    '..##. => .', '#.##. => #', '#.#.. => .', '##... => .', '..#.# => #', '#.### => #', '.#..# => .', '#...# => #',
    '.##.# => #', '.#.#. => #', '#..#. => #', '###.. => #', '...#. => .', '.#.## => #', '.##.. => .', '#..## => .',
    '##.## => .', '.#... => #', '#.#.# => .', '##..# => .', '....# => .', '..... => .', '...## => #', '##.#. => .',
]

combinations = {note[:5] for note in notes if note[-1] == '#'}

state = initial_state
zero_index = 0
for _ in range(GENERATIONS):
    if YES in state[:5]:
        state = NO + NO + state
        zero_index += 2
    if YES in state[-5:]:
        state += NO + NO

    new_state = ''
    for i in range(len(state)):
        if not 2 <= i < len(state) - 2:
            pass
        new_state += YES if state[i - 2: i + 3] in combinations else NO
    state = new_state

# part 1
positive_sum = sum(index for index, value in enumerate(state[zero_index:]) if value == YES)
negative_sum = sum(index for index, value in enumerate(state[zero_index::-1]) if value == YES)
print(positive_sum - negative_sum)


# part 2
partial_sum = positive_sum - negative_sum
magic_number = 2200  # found by printing large number of values
total_generations = 50000000000
print(partial_sum + 2200 * (total_generations // 100 - 2))
