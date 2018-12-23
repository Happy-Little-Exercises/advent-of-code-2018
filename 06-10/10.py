import re

PATTERN = re.compile('^position=< ?(-?\d+),  ?(-?\d+)> velocity=< ?(-?\d+),  ?(-?\d+)>$')

POINT = '#'
NO_POINT = ' '
GUESSED_LINE_HEIGHT = 15


def parse_point(point_):
    pos_x, pos_y, vel_x, vel_y = re.match(PATTERN, point_).groups()
    return (int(pos_x), int(pos_y)), (int(vel_x), int(vel_y))


def draw(data):
    max_x = max(px for px, _ in points)
    min_x = min(px for px, _ in points)
    max_y = max(py for _, py in points)
    min_y = min(py for _, py in points)
    area = [[NO_POINT for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for point_x, point_y in data:
        area[point_y - min_y][point_x - min_x] = POINT

    picture = '\n'.join(''.join(row) for row in area)

    # part 1
    print(picture)


with open("10_input.txt") as input_file:
    parsed_data = [parse_point(line.strip()) for line in input_file.readlines()]
    points, velocities = zip(*parsed_data)

    seconds = 0
    while True:
        seconds += 1
        points = [(pos[0] + vel[0], pos[1] + vel[1]) for pos, vel in zip(points, velocities)]
        if max(py for _, py in points) - min(py for _, py in points) <= GUESSED_LINE_HEIGHT:
            draw(points)

            # part 2
            print(seconds)
            break


