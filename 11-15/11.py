SERIAL_NUMBER = 7689

GRID_SIZE = 300


def serial_number(x, y):
    return ((((x + 10) * y + SERIAL_NUMBER) * (x + 10) // 100) % 10) - 5


grid = [
    [serial_number(x_coord, y_coord) for x_coord in range(1, GRID_SIZE + 1)] for y_coord in range(1, GRID_SIZE + 1)
]

# part 1
max_position = None
max_sum = -999
for y_coord in range(GRID_SIZE - 2):
    for x_coord in range(GRID_SIZE - 2):
        subgrid_sum = sum(sum(row[x_coord:x_coord + 3]) for row in grid[y_coord:y_coord + 3])
        if subgrid_sum > max_sum:
            max_position = (x_coord + 1, y_coord + 1)
            max_sum = subgrid_sum

print(max_position, max_sum)


# part 2
max_position = None
max_sum = -999
subgrid_size = 0
while subgrid_size <= 300:
    subgrid_size += 1
    for y_coord in range(GRID_SIZE - subgrid_size + 1):
        for x_coord in range(GRID_SIZE - subgrid_size + 1):
            subgrid_sum = sum(sum(row[x_coord:x_coord + subgrid_size]) for row in grid[y_coord:y_coord + subgrid_size])
            if subgrid_sum > max_sum:
                max_position = (x_coord + 1, y_coord + 1)
                max_sum = subgrid_sum
    print(max_position, subgrid_size)

