def part_one():
    content = open('input.txt', 'r').readline()
    x, y = content.split(' ')

    xmin, xmax = list(map(int, x.split('..')))
    ymin, ymax = list(map(int, y.split('..')))

    y_velocity = -1*ymin-1
    y = 0

    while y_velocity != 0:
        y += y_velocity
        y_velocity -= 1

    print(y)

def find_xs(x_min, x_max):
    x = 0
    x_inital_velocities = []
    iterations = 0
    velocity = 0

    while x < x_max:
        if sum(x_inital_velocities) >= x_min:
            x_inital_velocities.append(len(iterations))
            iterations += 1
        else:
            iterations += 1
            velocity += 1
            x += velocity

    print(x_inital_velocities)

def part_two():
    content = open('input.txt', 'r').readline()
    x, y = content.split(' ')

    xmin, xmax = list(map(int, x.split('..')))
    ymin, ymax = list(map(int, y.split('..')))

    result = 0

    for xvel in range(1, xmax+1):
        for yvel in range(ymin, -ymin):
            if target_hit((xvel, yvel), (xmin, xmax, ymin, ymax)):
                result += 1
    
    print(result)

def target_hit(velocities, target):
    pos = (0,0)
    positions = []
    while pos[0] <= target[1] and pos[1] >= target[2]:
        positions.append(pos)
        pos = (pos[0]+velocities[0], pos[1]+velocities[1])
        velocities = (max(0, velocities[0] - 1), velocities[1]-1)
    
    for position in positions:
        if target[0] <= position[0] <= target[1] and target[2] <= position[1] <= target[3]:
            return True
    return False


if __name__ == '__main__':
    part_one()
    part_two()