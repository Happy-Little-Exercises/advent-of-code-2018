movements = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

replacement_symbols = {
    '-': {
        '>': '>',
        '<': '<'
    },
    '|': {
        '^': '^',
        'v': 'v'
    },
    '/': {
        '^': '>',
        '<': 'v'
    },
    '\\': {
        '^': '<',
        '>': 'v'
    },
    '+': {
        'v': '@'
    }
}
cart_symbols = {'^', '>', 'v', '<'}


def print_(graph_):
    for line in graph_:
        print(''.join(line))


def get(position, graph_):
    y, x = position
    return graph_[y][x]


def set_value(value, position, graph_):
    y, x = position
    graph_[y][x] = value


def move(cart_, graph_):
    cart_symbol = get(cart_, graph_)
    new_position = tuple(sum(dimension) for dimension in zip(cart_, movements[cart_symbol]))
    old_symbol = get(new_position, graph_)
    set_value(replacement_symbols[old_symbol][cart_symbol], new_position, graph_)


with open("13_input.txt") as input_file:
    graph = [list(line.strip()) for line in input_file.readlines()]
    print_(graph)

    carts = [(y, x) for y, row in enumerate(graph) for x, _ in enumerate(row) if row[x] in cart_symbols]
    print(carts)

    while True:
        for cart in carts:
            move(cart, graph)
        print()
        print_(graph)
        break


