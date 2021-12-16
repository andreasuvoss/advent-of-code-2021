def find_neighbours(coordinate, max_x, max_y):
    x,y = coordinate

    neighbours = []

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0:
                continue
            elif i > max_x or j > max_y:
                continue
            elif i == x and j == y:
                continue
            elif i != x and j != y:
                continue
            else:
                neighbours.append((i,j))

    return neighbours

def dijkstra_three(source, unvisited, target):
    max_x, max_y = target
    non_inf_nodes = dict()
    non_inf_nodes[source] = 0

    path = []
    cost_grid = [[float('inf') for y in range(max_y+1)] for x in range(max_x+1)]
    visited = dict()

    total_time_merging_nodes = 0
    total_time_checking_neighbours = 0
    total_time_finding_next_node = 0

    total_nodes = unvisited.copy()

    while unvisited:
        if source == target:
            return unvisited[target][1]
        
        neighbours = [neighbour for neighbour in find_neighbours(source, max_x, max_y)]

        for neighbour in neighbours:
            new_distance = total_nodes[neighbour][0]+total_nodes[source][1]
            if new_distance < total_nodes[neighbour][1]:
                unvisited[neighbour] = (total_nodes[neighbour][0], new_distance, total_nodes[neighbour][2])
                total_nodes[neighbour] = (total_nodes[neighbour][0], new_distance, total_nodes[neighbour][2])
                non_inf_nodes[neighbour] = new_distance
                cost_grid[neighbour[1]][neighbour[0]] = new_distance

        visited[source] = unvisited[source]
        unvisited.pop(source)
        non_inf_nodes.pop(source)
    
        path.append(source)

        source = min(non_inf_nodes, key=non_inf_nodes.get)

    pprint.pprint(cost_grid)

def part_one():
    content = open('input.txt', 'r')

    grid_risk = []
    grid_distance = []
    grid_visited = []

    for line in content:
        line = line.replace('\n', '')

        y_r = [int(num) for num in line]
        y_d = [float('inf') for num in line]
        y_v = [False for num in line]
        grid_risk.append(y_r)
        grid_distance.append(y_d)
        grid_visited.append(y_v)

    grid_risk[0][0] = 0
    grid_distance[0][0] = 0
    max_x = len(grid_risk[0]) - 1
    max_y = len(grid_risk) - 1
    
    grid = dict()
    non_inf_node = dict()
    non_inf_node[(0,0)] = 0

    for y in range(len(grid_risk)):
        for x in range(len(grid_risk[y])):
            grid[(x,y)] = (grid_risk[y][x], grid_distance[y][x], grid_visited[y][x])

    print(dijkstra_three((0,0), grid, (max_x, max_y)))

def increase(y):
    if y == 9:
        return 1
    return y+1

def create_new_content(content):
    grid_risk = []

    for line in content:
        line = line.replace('\n', '')
        y_r = [int(num) for num in line]

        temp = y_r

        for i in range(4):
            temp = [increase(y) for y in temp]
            y_r.extend(temp)

        grid_risk.append(y_r)

    for i in range(len(grid_risk)*4):
        old_list = grid_risk[i]
        new_list = [increase(x) for x in old_list]

        grid_risk.append(new_list)

    new_content = []

    for line in grid_risk:
        new_content.append(''.join(list(map(str, line))))

    return new_content

def part_two():

    content = open('input.txt', 'r')

    content = create_new_content(content)

    grid_risk = []
    grid_distance = []
    grid_visited = []

    for line in content:
        y_r = [int(num) for num in line]
        y_d = [float('inf') for num in line]
        y_v = [False for num in line]
        grid_risk.append(y_r)
        grid_distance.append(y_d)
        grid_visited.append(y_v)

    grid_risk[0][0] = 0
    grid_distance[0][0] = 0
    max_x = len(grid_risk[0]) - 1
    max_y = len(grid_risk) - 1
    
    grid = dict()
    non_inf_node = dict()
    non_inf_node[(0,0)] = 0

    for y in range(len(grid_risk)):
        for x in range(len(grid_risk[y])):
            grid[(x,y)] = (grid_risk[y][x], grid_distance[y][x], grid_visited[y][x])

    print(dijkstra_three((0,0), grid, (max_x, max_y)))

if __name__ == "__main__":
    part_one()
    part_two()
    