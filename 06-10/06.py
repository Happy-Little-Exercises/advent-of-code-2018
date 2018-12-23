from collections import namedtuple

Coord = namedtuple('Coord', ['x', 'y', 'id_'])


def has_finite_area(observed_point, points_):
    return all([
        any([p.x < observed_point.x for p in points_]),
        any([p.x > observed_point.x for p in points_]),
        any([p.y < observed_point.y for p in points_]),
        any([p.y > observed_point.y for p in points_])
    ])


def manhattan_distance(point_, x_, y_):
    return abs(point_.x - x_) + abs(point_.y - y_)


with open("06_input.txt") as input_file:
    lines = (line.strip() for line in input_file.readlines())
    points = []

    for line in lines:
        x, y = line.split(', ')
        points.append(Coord(x=int(x), y=int(y), id_=line))

    min_x = min(coord.x for coord in points)
    max_x = max(coord.x for coord in points)
    min_y = min(coord.y for coord in points)
    max_y = max(coord.y for coord in points)

    available_locations = [(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)]

    # part 1
    neighbourhoods = {}
    finite_area_points = {point for point in points if has_finite_area(point, points)}
    for coord in available_locations:
        shortest_distance = None
        closest_point = None
        more_than_one_match = False
        for point in points:
            distance = manhattan_distance(point, *coord)
            if not closest_point or distance < shortest_distance:
                shortest_distance = distance
                closest_point = point
                more_than_one_match = False
            elif distance == shortest_distance:
                more_than_one_match = True

        if not more_than_one_match and closest_point in finite_area_points:
            neighbourhoods.setdefault(closest_point.id_, []).append(coord)

    print(max(len(value) for value in neighbourhoods.values()))

    # part 2
    area = []
    for coord in available_locations:
        if sum(manhattan_distance(point, *coord) for point in points) < 10000:
            area.append(coord)
    print(len(area))
