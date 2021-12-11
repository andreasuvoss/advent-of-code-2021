import pprint

def find_neighbouring_octopi(coordinate, max_x, max_y):
    x,y = coordinate
    neighbouring_octopi = []
    
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0:
                continue
            if i > max_x-1 or j > max_y-1:
                continue
            if i == x and j == y:
                continue
            neighbouring_octopi.append([i,j])

    return neighbouring_octopi

def flash_octopus(octopus, octopus_grid, flash_count):

    if octopus_grid[octopus[1]][octopus[0]] == 0:
        return octopus_grid, flash_count

    flash_count += 1

    max_x = len(octopus_grid[0])
    max_y = len(octopus_grid)

    octopus_grid[octopus[1]][octopus[0]] = 0
    neighbours = find_neighbouring_octopi([octopus[0], octopus[1]], max_x, max_y)

    for neighbour in neighbours:
        neighbour_value = octopus_grid[neighbour[1]][neighbour[0]]

        if neighbour_value == 0:
            continue
        else:
            octopus_grid[neighbour[1]][neighbour[0]] += 1

        if octopus_grid[neighbour[1]][neighbour[0]] > 9:
            octopus_grid, flash_count = flash_octopus([neighbour[0], neighbour[1]], octopus_grid, flash_count)

    return octopus_grid, flash_count

def step(octopus_grid):
    max_x = len(octopus_grid[0])
    max_y = len(octopus_grid)

    buffed_up_octopi = []

    flashed_octopi_this_step = 0

    for y in range(max_y):
        for x in range(max_x):
            octopus_grid[y][x] += 1
            if octopus_grid[y][x] > 9:
                buffed_up_octopi.append([x, y])

    for bufftopi in buffed_up_octopi:
        octopus_grid, flash_count = flash_octopus(bufftopi, octopus_grid, 0)
        flashed_octopi_this_step += flash_count

    return octopus_grid, flashed_octopi_this_step


def part_one():
    content = open('input.txt', 'r')
    octopus_grid = []

    for line in content:
        line = line.replace('\n', '')
        octopus_grid.append([int(ocotopus) for ocotopus in line])

    total_flashes = 0

    for i in range(100):
        octopus_grid, flash_count = step(octopus_grid)
        total_flashes += flash_count

    print(total_flashes)

def part_two():
    content = open('input.txt', 'r')
    octopus_grid = []

    for line in content:
        line = line.replace('\n', '')
        octopus_grid.append([int(ocotopus) for ocotopus in line])

    total_flashes = 0
    grid_size = len(octopus_grid) * len(octopus_grid[0])

    step_number = 0

    while True:
        octopus_grid, flash_count = step(octopus_grid)
        step_number += 1
        if flash_count == grid_size:
            break

    print(step_number)

if __name__ == "__main__":
    part_one()
    part_two()
    