def construct_map(nodes, node_mappings):
    all_node_targets = []

    for node in nodes:

        node_targets = []

        for node_mapping in node_mappings:
            if node == node_mapping[0]:
                node_targets.append(node_mapping[1])
            elif node == node_mapping[1]:
                node_targets.append(node_mapping[0])
        
        all_node_targets.append(node_targets)

    return dict(zip(nodes, all_node_targets))
            

def find_path(starting_node, visited_nodes, node_map, path_taken, found_paths):

    path_taken += starting_node+','

    if starting_node == 'end':
        found_paths.append(path_taken[:-1])
        return found_paths

    next_visited_nodes = []
    next_visited_nodes.extend(visited_nodes)

    if starting_node.islower():
        next_visited_nodes.append(starting_node)

    possible_target_nodes = [node for node in node_map[starting_node] if node not in visited_nodes]

    for node in possible_target_nodes:
        found_paths = find_path(node, next_visited_nodes, node_map, path_taken, found_paths)

    return found_paths

def find_longer_path(starting_node, visited_nodes, node_map, path_taken, found_paths, double_visit):
    # This is a bit slow hehe
    
    path_taken += starting_node+','

    if starting_node == 'end':
        found_paths.append(path_taken[:-1])
        return found_paths

    next_visited_nodes = []
    next_visited_nodes.extend(visited_nodes)

    if starting_node.islower():
        next_visited_nodes.append(starting_node)

    if double_visit:
        possible_target_nodes = [node for node in node_map[starting_node] if node not in visited_nodes]
    else:
        if starting_node.islower() and starting_node in visited_nodes:
            double_visit = True
            possible_target_nodes = [node for node in node_map[starting_node] if node not in visited_nodes]
        else:
            possible_target_nodes = [node for node in node_map[starting_node] if node != 'start']

    for node in possible_target_nodes:
        found_paths = find_longer_path(node, next_visited_nodes, node_map, path_taken, found_paths, double_visit)

    return found_paths

def part_one():
    content = open('input.txt', 'r')

    from_cave = []
    to_cave = []

    all_caves = []

    for line in content:
        line = line.replace('\n', '')
        caves = line.split('-')
        from_cave.append(caves[0])
        to_cave.append(caves[1])

    all_caves.extend(from_cave)
    all_caves.extend(to_cave)
    all_caves = set(all_caves)
    cave_mappings = list(zip(from_cave, to_cave))

    cave_map = construct_map(all_caves, cave_mappings)

    found_paths = find_path('start', [], cave_map, '', [])

    print(len(found_paths))

def part_two():
    content = open('/home/andreasvoss/repos/advent-of-code-2021/12/input.txt', 'r')

    from_cave = []
    to_cave = []

    all_caves = []

    for line in content:
        line = line.replace('\n', '')
        caves = line.split('-')
        from_cave.append(caves[0])
        to_cave.append(caves[1])

    all_caves.extend(from_cave)
    all_caves.extend(to_cave)
    all_caves = set(all_caves)
    cave_mappings = list(zip(from_cave, to_cave))

    cave_map = construct_map(all_caves, cave_mappings)

    found_paths = find_longer_path('start', [], cave_map, '', [], False)

    print(len(found_paths))


if __name__ == "__main__":
    part_one()
    part_two()
    