def part_one():
    # pretty naive approach
    content = open('input.txt', 'r')
    crab_positions = [int(crab) for crab in content.read().split(',')]
    possible_solutions = []

    for i in range(max(crab_positions)):
        fuel_spent = 0
        
        for pos in crab_positions:
            if pos > i:
                fuel_spent += pos - i
            elif pos < i:
                fuel_spent += i - pos

        possible_solutions.append(fuel_spent)

    print(min(possible_solutions))
            

def part_two():
    content = open('input.txt', 'r')
    crab_positions = [int(crab) for crab in content.read().split(',')]
    possible_solutions = []

    costs = [None] * (max(crab_positions)+1)

    for i in range(max(crab_positions)):
        fuel_spent = 0
        
        for pos in crab_positions:
            if pos > i:
                lookup = costs[pos - i]
                if lookup is None:
                    costs[pos - i] = sum([j for j in range(1, pos - i+1)])
                    fuel_spent += costs[pos - i]
                else:
                    fuel_spent += lookup
            elif pos < i:
                lookup = costs[i-pos] 
                if lookup is None:
                    costs[i-pos] = sum([j for j in range(1, i - pos+1)])
                    fuel_spent += costs[i-pos] 
                else:
                    fuel_spent += lookup

        possible_solutions.append(fuel_spent)

    print(min(possible_solutions))
    

if __name__ == "__main__":
    part_one()
    part_two()
    