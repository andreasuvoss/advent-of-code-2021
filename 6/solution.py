def part_one():
    # pretty naive approach
    content = open('input.txt', 'r')
    fishies = [int(fish) for fish in content.read().split(',')]

    days_to_monitor = 80

    for day in range(days_to_monitor):

        new_fishies = []

        for i in range(len(fishies)):
            if fishies[i] == 0:
                fishies[i] = 6
                new_fishies.append(8)
            else: 
                fishies[i] -= 1
        
        fishies.extend(new_fishies)

    print(len(fishies))
            

def group_fishies(fishies):
    
    grouped_fishies = [0]*9

    for fish in fishies:
        grouped_fishies[fish] += 1

    return grouped_fishies

def next_day(grouped_fishies):
    next_days_fish = [0]*9

    for i in range(len(grouped_fishies)):

        if i == len(grouped_fishies) - 1:
            next_days_fish[i] = grouped_fishies[0]
            next_days_fish[6] += grouped_fishies[0]
        else:
            next_days_fish[i] = grouped_fishies[i+1]

    return next_days_fish


def part_two():
    content = open('input.txt', 'r')
    fishies = [int(fish) for fish in content.read().split(',')]
    grouped_fishies = group_fishies(fishies)

    days_to_monitor = 256

    for day in range(days_to_monitor):
        grouped_fishies = next_day(grouped_fishies)
        
    print(sum(grouped_fishies))

if __name__ == "__main__":
    part_one()
    part_two()
    