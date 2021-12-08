def part_one():
    content = open('input.txt', 'r')

    signals = []
    outputs = []


    for line in content:
        signal_segment, output_segment = line.split(' | ')

        signals.append(signal_segment)
        outputs.append(list(map(lambda x : x.replace('\n', ''), output_segment.split(' '))))

    result = 0

    for output in outputs:
        for digit in output:
            if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                result += 1

    print(result)
            

def find_character_that_does_not_match(string_1, string_2):
    for letter in string_1:
        if letter not in string_2:
            return letter

def find_bottom_right_top_left_and_bottom_left_from_frequency(signal):
    letters = ['a','b','c','d','e','f','g']
    counter = [0]*7

    for digit in signal:
        for letter in digit:
            counter[letters.index(letter)] += 1

    return (letters[counter.index(9)], letters[counter.index(6)], letters[counter.index(4)])

g_number_mappings = [
    sorted(['TOP', 'BOTTOM', 'TOP_LEFT', 'BOTTOM_LEFT', 'TOP_RIGHT', 'BOTTOM_RIGHT']),
    sorted(['TOP_RIGHT', 'BOTTOM_RIGHT']),
    sorted(['TOP', 'BOTTOM', 'BOTTOM_LEFT', 'TOP_RIGHT', 'MIDDLE']),
    sorted(['TOP', 'BOTTOM', 'TOP_RIGHT', 'BOTTOM_RIGHT', 'MIDDLE']),
    sorted(['MIDDLE', 'TOP_RIGHT', 'BOTTOM_RIGHT', 'TOP_LEFT']),
    sorted(['TOP', 'BOTTOM', 'TOP_LEFT', 'MIDDLE', 'BOTTOM_RIGHT']),
    sorted(['TOP', 'MIDDLE', 'BOTTOM', 'TOP_LEFT', 'BOTTOM_LEFT', 'BOTTOM_RIGHT']),
    sorted(['TOP', 'TOP_RIGHT', 'BOTTOM_RIGHT']),
    sorted(['TOP', 'BOTTOM', 'TOP_LEFT', 'BOTTOM_LEFT', 'TOP_RIGHT', 'BOTTOM_RIGHT', 'MIDDLE']),
    sorted(['TOP', 'BOTTOM', 'TOP_LEFT', 'TOP_RIGHT', 'MIDDLE', 'BOTTOM_RIGHT'])
]

def map_output_to_number(output_digit, mappings):
    global g_number_mappings

    resulting_digit = []

    for char in output_digit:
        resulting_digit.append(mappings[char])
    
    resulting_digit = sorted(resulting_digit)

    for i in range(10):
        if g_number_mappings[i] == resulting_digit:
            return str(i)

def analyze_signal(signal):

    signal = sorted(signal, key=len)

    found_segments = []

    one = signal[0]
    seven = signal[1]
    four = signal[2]
    eight = signal[9]

    mappings = ['TOP', 'BOTTOM_RIGHT', 'TOP_LEFT', 'BOTTOM_LEFT', 'TOP_RIGHT', 'MIDDLE', 'BOTTOM']

    top_segment = find_character_that_does_not_match(seven, one)
    bottom_right, top_left, bottom_left = find_bottom_right_top_left_and_bottom_left_from_frequency(signal)
    found_segments.extend([top_segment, bottom_right, top_left, bottom_left])
    top_right = find_character_that_does_not_match(one, found_segments)
    found_segments.append(top_right)
    middle = find_character_that_does_not_match(four, found_segments)
    found_segments.append(middle)
    bottom = find_character_that_does_not_match(eight, found_segments)
    found_segments.append(bottom)
    return dict(zip(found_segments, mappings))



def part_two():
    content = open('input.txt', 'r')

    signals = []
    outputs = []


    for line in content:
        signal_segment, output_segment = line.split(' | ')

        signals.append(signal_segment.split(' '))
        outputs.append(list(map(lambda x : x.replace('\n', ''), output_segment.split(' '))))


    result_list = []

    for i in range(len(signals)):
        analyzed_signals = analyze_signal(signals[i])

        result = ""

        for output in outputs[i]:
            result += map_output_to_number(output, analyzed_signals)

        result_list.append(int(result))

    print(sum(result_list))

    # 1. find difference between 2 char and 3 char number this is TOP

    # 2. Find BOTTOM_RIGHT, TOP_LEFT and BOTTOM_LEFT from the frequency (9,6,4)

    # 3. of the chars in 2 char digit find the one used in 9 of the numbers this is BOTTOM_RIGHT. The other one in the 2 char digit must be TOP_RIGHT

    # 4. Look at 4, and the segment not found by now is the middle segment

    # 5. last segment. :)


    

if __name__ == "__main__":
    part_one()
    part_two()
    