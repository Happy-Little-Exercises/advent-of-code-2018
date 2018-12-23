def init_requirements(lines):
    requirements_ = {}
    for line in lines:
        predecessor, id_ = line[5], line[36]
        requirements_.setdefault(id_, set()).add(predecessor)
        requirements_.setdefault(predecessor, set())
    return requirements_


def mark_allowed_nodes(requirements_, allowed_nodes_, added_nodes_):
    for node_, requirements in requirements_.items():
        requirements -= added_nodes_
        if not requirements:
            allowed_nodes_.append(node_)


def sanitize(requirements_, allowed_nodes_):
    for node_ in allowed_nodes_:
        requirements_.pop(node_, None)


def worker(n):
    for _ in range(n):
        yield True
    yield False


MAX_WORKERS = 5

with open("07_input.txt") as input_file:
    input_ = [line.strip() for line in input_file.readlines()]

    # part 1
    node_requirements = init_requirements(input_)
    order = ""
    added_nodes = set()
    allowed_nodes = []

    while node_requirements:
        mark_allowed_nodes(node_requirements, allowed_nodes, added_nodes)

        if allowed_nodes:
            allowed_nodes = sorted(allowed_nodes)
            sanitize(node_requirements, allowed_nodes)
            next_node, allowed_nodes = allowed_nodes[0], allowed_nodes[1:]
            order += next_node
            added_nodes.add(next_node)

    print(order)

    # part 2
    node_requirements = init_requirements(input_)
    order = ""
    added_nodes = set()
    allowed_nodes = []

    workers = {}
    total_time = 0
    while node_requirements or allowed_nodes or workers:
        # update count and workers
        total_time += 1
        newly_added = [node for node, worker in workers.items() if not next(worker)]
        for node in newly_added:
            added_nodes.add(node)
            workers.pop(node)

        mark_allowed_nodes(node_requirements, allowed_nodes, added_nodes)

        # add new workers
        if allowed_nodes:
            allowed_nodes = sorted(allowed_nodes)
            sanitize(node_requirements, allowed_nodes)

            for _ in range(MAX_WORKERS - len(workers)):
                if allowed_nodes:
                    next_node, allowed_nodes = allowed_nodes[0], allowed_nodes[1:]
                    new_worker = worker(ord(next_node) - 5)  # 'A' => 1, 'B' => 2,... TODO fix
                    workers[next_node] = new_worker

    # TODO fix off by one error
    print(total_time - 1)
