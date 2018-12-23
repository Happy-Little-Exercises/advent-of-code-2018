from collections import namedtuple

Tree = namedtuple("Tree", ['children', 'metadata'])


def parse_tree(numbers):
    subtree_count, meta_count, numbers = numbers[0], numbers[1], numbers[2:]

    subtrees = []
    for _ in range(subtree_count):
        new_subtree, numbers = parse_tree(numbers)
        subtrees.append(new_subtree)

    return Tree(subtrees, numbers[:meta_count]), numbers[meta_count:]


def meta_sum(tree):
    return sum(tree.metadata) + sum(meta_sum(subtree) for subtree in tree.children)


def advanced_sum(tree):
    if tree.children:
        return sum(advanced_sum(tree.children[index - 1]) for index in tree.metadata if index <= len(tree.children))
    else:
        return sum(tree.metadata)


with open("08_input.txt") as input_file:
    input_ = [int(number) for number in input_file.read().strip().split(' ')]

    root_tree, _ = parse_tree(input_)

    # part 1
    print(meta_sum(root_tree))

    # part 2
    print(advanced_sum(root_tree))
