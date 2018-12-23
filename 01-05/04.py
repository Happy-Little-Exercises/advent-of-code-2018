import re
from collections import Counter

PATTERN = re.compile('^\[.+\] Guard #(\d+) begins shift$')

MINUTE_START = 15
MINUTE_END = 17


def key_with_max_value(dict_):
    return max(dict_, key=lambda k: dict_[k])


with open("04_input.txt") as input_file:
    input_ = sorted(line.strip() for line in input_file.readlines())
    sleep_minutes = {}

    current_guard = None
    current_start = None

    for line in input_:
        try:
            id_ = re.match(PATTERN, line).groups()[0]
            current_guard = int(id_)
        except AttributeError:
            if line[19:] == 'falls asleep':
                current_start = int(line[MINUTE_START:MINUTE_END])
            else:
                end = int(line[MINUTE_START:MINUTE_END])
                sleep_minutes.setdefault(current_guard, []).extend([minute for minute in range(current_start, end)])

    # part 1
    sleep_durations = {guard: len(minutes) for guard, minutes in sleep_minutes.items()}
    max_guard = key_with_max_value(sleep_durations)
    max_minute = Counter(sleep_minutes[max_guard]).most_common(1)[0][0]
    print(max_guard * max_minute)

    # part 2
    minute_counts = {guard: Counter(minutes) for guard, minutes in sleep_minutes.items()}
    max_counts = {guard: minutes.most_common(1)[0][1] for guard, minutes in minute_counts.items()}
    max_minute_guard = key_with_max_value(max_counts)
    print(max_minute_guard * minute_counts[max_minute_guard].most_common(1)[0][0])
