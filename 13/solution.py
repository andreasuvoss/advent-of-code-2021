def is_horizontal_fold_and_coordinate(fold):
    is_horizontal_fold = fold[0] is None

    if is_horizontal_fold:
        return True, fold[1]
    
    return False, fold[0]

def fold_vertical(folding_idx, transparent_paper, dots):
    
    new_dots = set([])
    
    for dot in dots:
        dot_x = dot[0]
        if dot_x < folding_idx:
            new_dots.add((dot[0], dot[1]))
        if dot_x > folding_idx:
            diff = dot_x - folding_idx
            transparent_paper[dot[1]][folding_idx-diff] = '#'

            new_dots.add((folding_idx-diff, dot[1]))
    
    for line in transparent_paper:
        while len(line) > folding_idx:
            line.pop()

    new_dots = [[dot[0], dot[1]] for dot in new_dots]

    return transparent_paper, new_dots


def fold_horizontal(folding_idx, transparent_paper, dots):

    new_dots = set([])

    for dot in dots:
        dot_y = dot[1]
        if dot_y < folding_idx:
            new_dots.add((dot[0], dot[1]))
        if dot_y > folding_idx:
            diff = dot_y - folding_idx
            transparent_paper[folding_idx-diff][dot[0]] = '#'
            
            new_dots.add((dot[0], folding_idx-diff))

    while len(transparent_paper) > folding_idx:
        transparent_paper.pop()

    new_dots = [[dot[0], dot[1]] for dot in new_dots]

    return transparent_paper, new_dots

def part_one():
    content = open('input.txt', 'r')

    fold_input = False
    largest_x = 0
    largest_y = 0
    dots = []
    folds = []

    for line in content:
        line = line.replace('\n', '')
        if line == '':
            fold_input = True
            continue

        if not fold_input:
            x,y = list(map(int, line.split(',')))
            if x > largest_x:
                largest_x = x
            if y > largest_y:
                largest_y = y
            dots.append([x,y])
        else:
            axis, coordinate = line.split(' ')[2].split('=')
            if axis == 'x':
                folds.append([int(coordinate), None])
            else:
                folds.append([None, int(coordinate)])

    transparent_paper = [['.' for x in range(largest_x+1)] for y in range(largest_y+1)]

    first_fold = folds[0]

    is_horizontal, idx = is_horizontal_fold_and_coordinate(first_fold)
    if is_horizontal:
        transparent_paper, dots = fold_horizontal(idx, transparent_paper, dots)
        print(len(dots))
    else:
        transparent_paper, dots = fold_vertical(idx, transparent_paper, dots)
        print(len(dots))

def part_two():
    content = open('input.txt', 'r')

    fold_input = False
    largest_x = 0
    largest_y = 0
    dots = []
    folds = []

    for line in content:
        line = line.replace('\n', '')
        if line == '':
            fold_input = True
            continue

        if not fold_input:
            x,y = list(map(int, line.split(',')))
            if x > largest_x:
                largest_x = x
            if y > largest_y:
                largest_y = y
            dots.append([x,y])
        else:
            axis, coordinate = line.split(' ')[2].split('=')
            if axis == 'x':
                folds.append([int(coordinate), None])
            else:
                folds.append([None, int(coordinate)])

    transparent_paper = [['.' for x in range(largest_x+1)] for y in range(largest_y+1)]

    for i, fold in enumerate(folds):
        is_horizontal, idx = is_horizontal_fold_and_coordinate(fold)
        if is_horizontal:
            transparent_paper, dots = fold_horizontal(idx, transparent_paper, dots)
        else:
            transparent_paper, dots = fold_vertical(idx, transparent_paper, dots)

    for line in transparent_paper:
        print(''.join(line))


if __name__ == "__main__":
    part_one()
    part_two()
    