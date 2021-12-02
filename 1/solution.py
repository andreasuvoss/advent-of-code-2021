
def load_input():
    content = open("input.txt", "r")
    

    return

def part_one():
    content = open("input.txt", "r")
    previous_measurement = None
    number_of_increased_measurements = 0
    
    for str_measurement in content:
        measurement = int(str_measurement)
        if previous_measurement is None:
            previous_measurement = measurement
            continue

        if measurement > previous_measurement:
            number_of_increased_measurements += 1

        previous_measurement = measurement

    print (number_of_increased_measurements)

def part_two():
    content = open("input.txt", "r")

    previous_sliding_window_measurement = None
    number_of_increased_slidingwindow_measurements = 0

    values_as_int_list = [int(line) for line in content]

    for i in range(len(values_as_int_list)-2):
        measurement = sum([values_as_int_list[i], values_as_int_list[i+1], values_as_int_list[i+2]])
        if previous_sliding_window_measurement is None:
            previous_sliding_window_measurement = measurement
            continue

        if measurement > previous_sliding_window_measurement:
            number_of_increased_slidingwindow_measurements += 1

        previous_sliding_window_measurement = measurement

    print(number_of_increased_slidingwindow_measurements)

if __name__ == "__main__":
    part_one()
    part_two()