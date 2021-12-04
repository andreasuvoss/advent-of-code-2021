
def check_board(seen_list):
    if all(seen_list[0:5]):
       return True
    elif all(seen_list[5:10]):
       return True
    elif all(seen_list[10:15]):
       return True
    elif all(seen_list[15:20]):
       return True
    elif all(seen_list[20:25]):
       return True
    elif all(seen_list[::5]):
       return True
    elif all(seen_list[1::5]):
       return True
    elif all(seen_list[2::5]):
       return True
    elif all(seen_list[3::5]):
       return True
    elif all(seen_list[4::5]):
       return True
    return False


def sum_of_unmarked_numbers(board, seen):
    sum_of_unmarked = 0
    
    for idx, has_been_seen in enumerate(seen):
        if not has_been_seen:
            sum_of_unmarked += board[idx]

    return sum_of_unmarked


def part_one():
    content = open('input.txt', 'r')
    numbers_to_be_called_needs_loading = True

    numbers_to_be_called = []
    boards = []

    for line in content:
        if numbers_to_be_called_needs_loading:
            numbers_to_be_called = map(int, line.split(','))
            numbers_to_be_called_needs_loading = False

        if (line == "\n"):
            seen = [False] * 25
            board = []
            for j in range(5):
                for num in content.__next__().split(' '):
                    if num == '':
                        continue
                    board.append(int(num))

            boards.append((board, seen))
        

    for called_number in numbers_to_be_called:
        for i, seen_board in enumerate(boards):

            board, seen = seen_board

            for j, board_number in enumerate(board):
                if called_number == board_number:
                    seen[j] = True

                winner = check_board(seen)

                if winner:
                    nice_sum = sum_of_unmarked_numbers(board, seen)
                    print("Part 1:", nice_sum, "*", called_number, "=", nice_sum*called_number)
                    break
            if winner:
                break
            boards[i] = (board, seen)
        if winner:
            break

def part_two():
    content = open('input.txt', 'r')
    numbers_to_be_called_needs_loading = True

    numbers_to_be_called = []
    boards = []

    for line in content:
        if numbers_to_be_called_needs_loading:
            numbers_to_be_called = map(int, line.split(','))
            numbers_to_be_called_needs_loading = False

        if (line == "\n"):
            seen = [False] * 25
            board = []
            for j in range(5):
                for num in content.__next__().split(' '):
                    if num == '':
                        continue
                    board.append(int(num))

            boards.append((board, seen))

    winners = [None] * len(boards)
    winner_number = 0
    last_called_num = 0
    found_all_winners = False

    for called_number in numbers_to_be_called:
        last_called_num = called_number
        for i, seen_board in enumerate(boards):

            board, seen = seen_board

            for j, board_number in enumerate(board):
                if called_number == board_number:
                    seen[j] = True

                winner = check_board(seen)

                if winner:
                    if winners[i] is None:
                        winners[i] = winner_number
                        winner_number += 1
            boards[i] = (board, seen)

            if all(map(lambda w : w is not None, winners)):
                found_all_winners = True
                break

        if found_all_winners:
            break

    idx = winners.index(max(winners))
    
    board, seen = boards[idx]
    nice_sum = sum_of_unmarked_numbers(board, seen)
    print("Part 2:", nice_sum, "*", last_called_num, "=", nice_sum*last_called_num)

if __name__ == "__main__":
    part_one()
    part_two()