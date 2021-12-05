import pprint

def line_is_horizontal_or_vertical(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return True
    return False

def split_coordinates(line):
    split_on_arrow = line.split('->')

    from_coordinates = list(map(int, split_on_arrow[0].split(',')))
    to_coordinates = list(map(lambda x : int(x.replace('\n', '')), split_on_arrow[1].split(',')))
    x1 = from_coordinates[0]
    y1 = from_coordinates[1]

    x2 = to_coordinates[0]
    y2 = to_coordinates[1]

    return x1, y1, x2, y2

def coordinates_in_straight_line(x1, y1, x2, y2):
    
    if x1 > x2:
        x_range = range(x2, x1+1)
    else:
        x_range = range(x1, x2+1)

    if y1 > y2:
        y_range = range(y2, y1+1)
    else:
        y_range = range(y1, y2+1)

    # vertical
    if x1 != x2 and y1 == y2:
        return [(i, y1) for i in x_range]

    # horizontal
    if y1 != y2 and x1 == x2:
        return [(x1, i) for i in y_range]

def coordinates_in_diagonal_line(x1, y1, x2, y2):
    coordinates = []

    if x1 > x2:
        y = y2
        y2 = y1
        y1 = y
        x_range = range(x2, x1+1)
    else:
        x_range = range(x1, x2+1)

    if y1 > y2:
        y_direction = -1
    else:
        y_direction = 1

    counter = 0

    for i in x_range:
        coordinates.append((i, y1+(counter*y_direction)))
        counter += 1
    return coordinates

    

def part_one():
    content = open('input.txt', 'r')

    coordinate_system = [[0 for x in range(1000)] for y in range(1000)]

    for line in content:
        x1, y1, x2, y2 = split_coordinates(line)

        if not line_is_horizontal_or_vertical(x1, y1, x2, y2):
            continue

        for coordinate in coordinates_in_straight_line(x1, y1, x2, y2):
            x, y = coordinate
            coordinate_system[x][y] += 1

    points_with_more_than_1_line = 0

    for row in coordinate_system:
        for value in row:
            if value > 1:
                points_with_more_than_1_line += 1

    print(points_with_more_than_1_line)

def part_two():
    content = open('input.txt', 'r')

    coordinate_system = [[0 for x in range(1000)] for y in range(1000)]

    for line in content:
        x1, y1, x2, y2 = split_coordinates(line)

        if not line_is_horizontal_or_vertical(x1, y1, x2, y2):
            for coordinate in coordinates_in_diagonal_line(x1, y1, x2, y2):
                x, y = coordinate
                coordinate_system[x][y] += 1
        else:
            for coordinate in coordinates_in_straight_line(x1, y1, x2, y2):
                x, y = coordinate
                coordinate_system[x][y] += 1

    points_with_more_than_1_line = 0

    for row in coordinate_system:
        for value in row:
            if value > 1:
                points_with_more_than_1_line += 1

    print(points_with_more_than_1_line)

if __name__ == "__main__":
    part_one()
    part_two()