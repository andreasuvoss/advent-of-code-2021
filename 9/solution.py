

def part_one():
    # This could be done more efficiently, but since the dataset
    # is so small, there is no need to overengineer anything

    content = open('input.txt', 'r')

    heightmap = [[0 for x in range(100)] for y in range(100)]

    for i, line in enumerate(content):

        line = line.replace('\n', '')

        for j, char in enumerate(line):
            heightmap[i][j] = int(char)


    minimum_values = []

    for x in range(len(heightmap[0])):
        for y in range(len(heightmap)):
            current_value = heightmap[y][x]
            value_above = value_below = value_right = value_left = 999

            if y != len(heightmap)-1:
                value_above = heightmap[y+1][x]
            if y != 0:
                value_below = heightmap[y-1][x]
            if x != len(heightmap[0])-1:
                value_right = heightmap[y][x+1]
            if x != 0:
                value_left = heightmap[y][x-1]

            if current_value < value_above and current_value < value_below and current_value < value_left and current_value < value_right:
                minimum_values.append(current_value)
    
    print(sum([value+1 for value in minimum_values]))

def transform_input():
    content = open('input.txt', 'r')

    improved_content = ""

    for line in content:
        line = line.replace('\n', '')
        improved_line = ""
        for char in line:
            if char != "9":
                improved_line += "."
            else:
                improved_line += "9"
        improved_line += '\n'
        improved_content += improved_line
    
    with open('better_input.txt', 'w') as f:
        f.write(improved_content)

def find_neighbouring_coordinates(coordinate, max_x, max_y):
    x,y = coordinate
    neighbouring_coordinates = []
    
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0:
                continue
            if i > max_x or j > max_y:
                continue
            if i == x and j == x:
                continue
            if i == x-1 and j == y-1:
                continue
            if i == x+1 and j == y+1:
                continue
            if i == x-1 and j == y+1:
                continue
            if i == x+1 and j == y-1:
                continue
            neighbouring_coordinates.append([i,j])

    return neighbouring_coordinates

def explore_basin(starting_coordinate, explored_coordinates, basin_coordinates, basin_map):
    map_size = len(basin_map)-1

    y = starting_coordinate[1]
    x = starting_coordinate[0]

    if basin_map[y][x] == '9':
        explored_coordinates.append(starting_coordinate)
        return explored_coordinates, basin_coordinates
    elif [x,y] in explored_coordinates:
        return explored_coordinates, basin_coordinates
    else:
        basin_coordinates.append(starting_coordinate)
        explored_coordinates.append(starting_coordinate)

    neighbours_to_explore = find_neighbouring_coordinates(starting_coordinate, map_size, map_size)

    for neighbour in neighbours_to_explore:
        if neighbour in explored_coordinates:
            continue
        explored_coordinates, basin_coordinates = explore_basin(neighbour, explored_coordinates, basin_coordinates, basin_map)

    return explored_coordinates, basin_coordinates

def find_starting_point_for_basin(unexplored_coordinates, basin_map):
    indicies_to_remove = []
    
    for i, coordinate in enumerate(unexplored_coordinates):
        if basin_map[coordinate[1]][coordinate[0]] != '9':
            return [coordinate[0], coordinate[1]], indicies_to_remove
        else:
            indicies_to_remove.append(i)
    
    return None, None

def part_two():
    # This code is so bad and inefficient
    # but atleast I reached the correct result in the end

    content = open('better_input.txt', 'r')

    basin_map = [[0 for x in range(100)] for y in range(100)]

    explored_coordinates = []
    basin_coordinates = []
    unexplored_coordinates = []

    for y, line in enumerate(content):

        line = line.replace('\n', '')

        for x, char in enumerate(line):
            basin_map[y][x] = char
            unexplored_coordinates.append([x, y])

    all_basins = []

    while len(unexplored_coordinates) > 0:
        basin_coordinates = []
        starting_point, throw_away_coords = find_starting_point_for_basin(unexplored_coordinates, basin_map)

        if starting_point is None:
            break

        for idx in throw_away_coords:
            unexplored_coordinates.pop(idx)
        explored_coordinates, basin_coordinates = explore_basin(starting_point, explored_coordinates, basin_coordinates, basin_map)
        unexplored_coordinates = [unexp for unexp in unexplored_coordinates if unexp not in explored_coordinates]
        explored_coordinates = []
        all_basins.append(len(basin_coordinates))

    largest_basins = sorted(all_basins, reverse=True)[:3]

    #print(all_basins)
    #print(largest_basins)
    product = 1
    for num in largest_basins:
        product *= num
    print(product)


if __name__ == "__main__":
    part_one()
    part_two()
    