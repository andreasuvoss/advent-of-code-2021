def step(template, polymer_mapping):
    result = []
    injecting_letters = []

    for i in range(len(template)-1):
        
        pair = template[i]+template[i+1]
        result.append(template[i])
        result.append(polymer_mapping[pair])
    
    result.append(template[-1])

    return ''.join(result)

def part_one():
    content = open('input.txt', 'r')

    template = ''
    keys = []
    values = []

    for i, line in enumerate(content):
        line = line.replace('\n', '')

        if i == 0:
            template = line
        elif i == 1:
            continue
        else:
            key, value = line.split(' -> ')
            keys.append(key)
            values.append(value)

    polymer_mapping = dict(zip(keys, values))

    steps_to_take = 10

    for i in range(steps_to_take):
        template = step(template, polymer_mapping)

    letter_map = dict(zip(set(template), [0] * len(set(template))))

    for letter in template:
        letter_map[letter] += 1

    sorted_letter_tuples = sorted(letter_map.items(), key=lambda item: item[1])

    most_common_letter_number_of_occurrences = sorted_letter_tuples[-1][1]
    least_common_letter_number_of_occurrences = sorted_letter_tuples[0][1]

    print(most_common_letter_number_of_occurrences-least_common_letter_number_of_occurrences)

def convert_template_to_map(template):

    template_map = dict()
    letter_count = dict()

    for i in range(len(template)-1):
        if template[i]+template[i+1] not in template_map:
            template_map[template[i]+template[i+1]] = 1
        else:
            template_map[template[i]+template[i+1]] += 1

    for letter in template:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    return template_map, letter_count

def better_step(template, letter_count, polymer_mapping, number_of_steps):
    if number_of_steps == 0:
        return template, letter_count

    empty_template = dict()

    for pair in template:
        letter = polymer_mapping[pair]
        pair_one = pair[0] + letter
        pair_two = letter + pair[1]

        number_of_original_pairs = template[pair]

        if letter not in letter_count:
            letter_count[letter] = 1 * number_of_original_pairs
        else:
            letter_count[letter] += 1 * number_of_original_pairs
        if pair_one not in empty_template:
            empty_template[pair_one] = 1 * number_of_original_pairs
        else:
            empty_template[pair_one] += 1 * number_of_original_pairs

        if pair_two not in empty_template:
            empty_template[pair_two] = 1 * number_of_original_pairs
        else:
            empty_template[pair_two] += 1 * number_of_original_pairs

    return better_step(empty_template, letter_count, polymer_mapping, number_of_steps-1)
    
def part_two():
    content = open('input.txt', 'r')

    template = ''
    keys = []
    values = []

    for i, line in enumerate(content):
        line = line.replace('\n', '')

        if i == 0:
            template = line
        elif i == 1:
            continue
        else:
            key, value = line.split(' -> ')
            keys.append(key)
            values.append(value)

    polymer_mapping = dict(zip(keys, values))
    template_map, letter_count = convert_template_to_map(template)

    depth = 40
    template_map, letter_count = better_step(template_map, letter_count, polymer_mapping, depth)

    sorted_letter_count = sorted(letter_count.items(), key=lambda item: item[1])

    most_common_letter_number_of_occurrences = sorted_letter_count[-1][1]
    least_common_letter_number_of_occurrences = sorted_letter_count[0][1]

    print(most_common_letter_number_of_occurrences-least_common_letter_number_of_occurrences)

if __name__ == "__main__":
    part_one()
    part_two()
    