import math

def from_hex_to_bin(hex_value):
    lookup_table = {
        '0' : str(bin(int('0', 16))[2:].zfill(4)),
        '1' : str(bin(int('1', 16))[2:].zfill(4)),
        '2' : str(bin(int('2', 16))[2:].zfill(4)),
        '3' : str(bin(int('3', 16))[2:].zfill(4)),
        '4' : str(bin(int('4', 16))[2:].zfill(4)),
        '5' : str(bin(int('5', 16))[2:].zfill(4)),
        '6' : str(bin(int('6', 16))[2:].zfill(4)),
        '7' : str(bin(int('7', 16))[2:].zfill(4)),
        '8' : str(bin(int('8', 16))[2:].zfill(4)),
        '9' : str(bin(int('9', 16))[2:].zfill(4)),
        'A' : str(bin(int('A', 16))[2:].zfill(4)),
        'B' : str(bin(int('B', 16))[2:].zfill(4)),
        'C' : str(bin(int('C', 16))[2:].zfill(4)),
        'D' : str(bin(int('D', 16))[2:].zfill(4)),
        'E' : str(bin(int('E', 16))[2:].zfill(4)),
        'F' : str(bin(int('F', 16))[2:].zfill(4))
    }

    bin_value = ''

    for char in hex_value:
        bin_value += lookup_table[char]

    return [val for val in bin_value]

def compute_subpackets(subpacket_values, type_id):
    
    type_id = int(''.join(type_id), 2)

    if type_id == 0:
        return sum(subpacket_values)
    if type_id == 1:
        return math.prod(subpacket_values)
    if type_id == 2:
        return min(subpacket_values)
    if type_id == 3:
        return max(subpacket_values)
    if type_id == 5:
        if subpacket_values[0] > subpacket_values[1]: return 1
        return 0
    if type_id == 6:
        if subpacket_values[0] < subpacket_values[1]: return 1
        return 0
    if type_id == 7:
        if subpacket_values[0] == subpacket_values[1]: return 1
        return 0
            
def parse_packet(packet, starting_bit_idx, version):
    current_idx = starting_bit_idx
    packet_version = packet[current_idx:current_idx+3]
    current_idx += 3
    packet_type_id = packet[current_idx:current_idx+3]
    current_idx += 3
    packet_is_literal = packet_type_id == ['1', '0', '0']
    version += int(''.join(packet_version), 2)

    if packet_is_literal:
        literal_packet_value = []
        while True:
            is_last_packet = packet[current_idx] == '0'
            literal_packet_value.extend(packet[current_idx+1:current_idx+5])
            current_idx += 5
            if is_last_packet:
                break
        return int(''.join(literal_packet_value), 2), current_idx, version
    else:
        length_type_id = packet[current_idx]
        current_idx += 1
        if length_type_id == '0':
            length = packet[current_idx:current_idx+15]
            current_idx += 15
            sub_packet_end_idx = int(''.join(length), 2) + current_idx
            subpacket_values = []

            while sub_packet_end_idx > current_idx:
                subpacket_value, current_idx, version = parse_packet(packet, current_idx, version)
                subpacket_values.append(subpacket_value)

            return compute_subpackets(subpacket_values, packet_type_id), current_idx, version
        else:
            length = packet[current_idx:current_idx+11]
            current_idx += 11
            subpacket_values = []

            for i in range(int(''.join(length),2)):
                subpacket_value, current_idx, version = parse_packet(packet, current_idx, version)
                subpacket_values.append(subpacket_value)

            return compute_subpackets(subpacket_values, packet_type_id), current_idx, version

def part_one():
    content = open('input.txt', 'r')
    hex_packet = content.readline()
    bin_packet = from_hex_to_bin(hex_packet)

    _, _, version_sum = parse_packet(bin_packet, 0, 0)

    print(version_sum)

def part_two():
    content = open('input.txt', 'r')
    hex_packet = content.readline()
    bin_packet = from_hex_to_bin(hex_packet)

    result, _, _ = parse_packet(bin_packet, 0, 0)

    print(result)

if __name__ == '__main__':
    part_one()
    part_two()