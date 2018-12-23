from collections import Counter


# part 1
def has_count(n, counter):
    return any(value == n for value in counter.values())


with open("02_input.txt") as input_file:
    counts = [Counter(word.strip()) for word in input_file.readlines()]
    twos = sum(has_count(2, word) for word in counts)
    threes = sum(has_count(3, word) for word in counts)
    print(twos * threes)

    # one-liner:
    print(sum(any(v == 2 for v in w.values()) for w in counts) * sum(any(v == 3 for v in w.values()) for w in counts))

# part 2
with open("02_input.txt") as input_file:
    words = [word.strip() for word in input_file.readlines()]
    for index, word in enumerate(words):
        for word2 in words[index + 1:]:
            match = (''.join(l1 for l1, l2 in zip(word, word2) if l1 == l2))
            if len(match) + 1 == len(word):
                print(match)
                break

    # one-liner:
    print(next(e for e in [[''.join(l1 for l1, l2 in zip(w1, w2) if l1 == l2) for w1 in words if sum(l1 != l2 for l1, l2 in zip(w1, w2)) == 1] for w2 in words] if e)[0])
