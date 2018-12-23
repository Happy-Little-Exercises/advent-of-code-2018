import string


def react(text_):
    i = 0
    while i < len(text_) - 1:
        char_ = text_[i]
        opposite = char_.upper() if char_.islower() else char_.lower()
        if text_[i + 1] == opposite:
            del text_[i: i + 2]
            if i:
                i -= 1
        else:
            i += 1
    return text_


with open("05_input.txt") as input_file:
    text = input_file.read().strip()

    # part 1
    print(len(react(list(text))))

    # part 2
    counts = {}
    for letter in string.ascii_lowercase:
        counts[letter] = len(react(list(text.replace(letter, '').replace(letter.upper(), ''))))
    print(min(counts.values()))
