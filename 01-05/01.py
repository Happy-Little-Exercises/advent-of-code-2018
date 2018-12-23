import itertools

# part 1
with open("01_input.txt") as input_file:
    input_ = '0' + ''.join(line.strip() for line in input_file.readlines())
    print(eval(input_))

# part 2
with open("01_input.txt") as input_file:
    input_lines = (int(line.strip()) for line in input_file.readlines())
    input_cycle = itertools.cycle(input_lines)
    frequencies = {0}
    current_frequency = 0

    while True:
        next_input = next(input_cycle)
        current_frequency = current_frequency + next_input
        if current_frequency in frequencies:
            print(current_frequency)
            break
        else:
            frequencies.add(current_frequency)
