def part_one():
    content = open("input.txt", "r")

    horizontal_position = 0
    depth = 0

    for command in content:
        command_split = command.split(' ')
        direction = command_split[0]
        distance = int(command_split[1])

        (horizontal_change, depth_change) = move(direction, distance)

        horizontal_position = horizontal_change + horizontal_position
        depth = depth + depth_change

    print(horizontal_position*depth)
        

def move(command, distance):
    if (command == 'forward'):
        return (distance, 0)
    if (command == 'up'):
        return (0, -distance)
    if (command == 'down'):
        return (0, distance)

    

def part_two():

    content = open("input.txt", "r")

    horizontal_position = 0
    depth = 0
    aim = 0

    for command in content:
        command_split = command.split(' ')
        cmd = command_split[0]
        change = int(command_split[1])

        if (cmd == 'forward'):
            horizontal_position += change
            depth += aim*change
        elif (cmd == 'up'):
            aim -= change
        elif (cmd == 'down'):
            aim += change

    print(horizontal_position*depth)

if __name__ == "__main__":
    part_one()
    part_two()