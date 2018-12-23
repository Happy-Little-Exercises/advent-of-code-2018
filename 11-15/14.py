NUMBER_OF_RECIPES = 509671
NUMBER_STRING = str(NUMBER_OF_RECIPES)
LAST_DIGIT = str(NUMBER_OF_RECIPES % 10)


# part 1
elf1 = 0
elf2 = 1
recipes = [3, 7]

while len(recipes) < NUMBER_OF_RECIPES + 10:
    recipes.extend(int(digit) for digit in str(recipes[elf1] + recipes[elf2]))

    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

print(''.join(str(value) for value in recipes[NUMBER_OF_RECIPES:]))


# part 2
elf1 = 0
elf2 = 1
recipes = [3, 7]
iterations = []
while True:
    new_digits = str(recipes[elf1] + recipes[elf2])
    iterations.append(len(new_digits))
    recipes.extend(int(digit) for digit in new_digits)

    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

    match_string = None
    semilast = False
    if new_digits == LAST_DIGIT:
        match_string = ''.join(str(value) for value in recipes[-5:])
    elif len(new_digits) == 2:
        if new_digits[0] == LAST_DIGIT:
            match_string = ''.join(str(value) for value in recipes[-6:-1])
            semilast = True
        elif new_digits[1] == LAST_DIGIT:
            # does not work if NUMBER_OF_RECIPES ends with duplicate digit
            match_string = ''.join(str(value) for value in recipes[-5:])

    if NUMBER_STRING == match_string:
        index = len(iterations) - 1
        print(index)
        required_count = 6 if semilast else 5
        while required_count > 0:
            required_count -= iterations[index]
            index -= 1
        print(index)
        break



