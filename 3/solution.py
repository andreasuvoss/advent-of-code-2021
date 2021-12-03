g_most_common = ""
g_least_common = ""

def flip_binary(binary):
    result = ""
    for i in range(len(binary)):
        if binary[i] == '0':
            result += '1'
        elif binary[i] == '1':
            result += '0'
    return result


def part_one():
    content = open('input.txt', 'r')

    bin_num_size = 0
    total_input_size = 0
    number_of_times_bit_is_one = None

    for binary in content:
        if number_of_times_bit_is_one is None:
            bin_num_size = len(binary)
            number_of_times_bit_is_one = [0] * (bin_num_size-1)

        for i in range(len(binary)):
            if binary[i] == '1':
                number_of_times_bit_is_one[i] += 1
        total_input_size += 1
        
    half_input_size = total_input_size / 2

    result = ""

    for i in range(bin_num_size-1):
        if number_of_times_bit_is_one[i] > half_input_size:
            result += '1'
        else:
            result += '0'

    flipped_result = flip_binary(result)

    print("Part 1:", int(result, 2) * int(flipped_result, 2))

def compute_most_common_bit(list_of_bits, keeping_bit):
    ones = 0
    zeroes = 0

    for bit in list_of_bits:
        if bit == 1:
            ones += 1
        elif bit == 0:
            zeroes += 1
    
    if ones > zeroes:
        return 1
    if ones == zeroes:
        if keeping_bit == 1:
            return 1
    return 0

def flip_bit(bit):
    if bit == 1:
        return 0
    return 1

def recursive_oxy(binary_list, bit_idx):
    if len(binary_list) == 1:
        return binary_list[0]

    list_for_next_run = []
    most_common_bit = compute_most_common_bit([int(binary[bit_idx]) for binary in binary_list], 1)

    for binary in binary_list:
        if int(binary[bit_idx]) == most_common_bit:
            list_for_next_run.append(binary)

    return recursive_oxy(list_for_next_run, bit_idx+1)

def recursive_co2(binary_list, bit_idx):
    if len(binary_list) == 1:
        return binary_list[0]

    list_for_next_run = []
    least_common_bit = flip_bit(compute_most_common_bit([int(binary[bit_idx]) for binary in binary_list], 1))

    for binary in binary_list:
        if int(binary[bit_idx]) == least_common_bit:
            list_for_next_run.append(binary)

    return recursive_co2(list_for_next_run, bit_idx+1)

def part_two():
    content = open('input.txt', 'r')
    binary_list = [binary[0:12] for binary in content]
    
    oxygen_generator_rating = recursive_oxy(binary_list, 0)
    co2_scrubber_rating = recursive_co2(binary_list, 0)

    print("Part 2:", int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))



if __name__ == "__main__":
    part_one()
    part_two()