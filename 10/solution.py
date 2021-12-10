def is_opening_symbol(symbol):
    if symbol == '(' or symbol == '[' or symbol == '{' or symbol == '<':
        return True
    return False

def part_one():
    content = open('input.txt', 'r')
    navigation_subsystem = []

    for line in content:
        line = line.replace('\n', '')
        navigation_subsystem.append([symbol for symbol in line])

    illegal_symbols = []

    for line in navigation_subsystem:
        illegal_symbols.append(check_if_line_is_corrupt_and_return_illegal_symbol(line))

    print(compute_score_syntax_errors(illegal_symbols))

def compute_score_syntax_errors(illegal_symbols):
    symbols = {
        '' : 0,
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137
    }

    score = 0

    for symbol in illegal_symbols:
        score += symbols[symbol]

    return score

def check_if_line_is_corrupt_and_return_illegal_symbol(line):
    symbols = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>'
    }

    allowed_closing_symbol_order = []

    illegal_symbol = ''

    for symbol in line:
        if not is_opening_symbol(symbol):
            if symbol != allowed_closing_symbol_order[-1]:
                illegal_symbol = symbol
                break
            else:
                allowed_closing_symbol_order.pop()
                continue
        
        allowed_closing_symbol_order.append(symbols[symbol])
    
    return illegal_symbol

def check_if_line_is_corrupt_and_return_legal_sequence(line):
    symbols = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>'
    }

    allowed_closing_symbol_order = []

    for symbol in line:
        if not is_opening_symbol(symbol):
            if symbol != allowed_closing_symbol_order[-1]:
                illegal_symbol = symbol
                return None
            else:
                allowed_closing_symbol_order.pop()
                continue
        
        allowed_closing_symbol_order.append(symbols[symbol])
    
    return allowed_closing_symbol_order[::-1]


    
def part_two():
    content = open('input.txt', 'r')
    navigation_subsystem = []

    for line in content:
        line = line.replace('\n', '')
        navigation_subsystem.append([symbol for symbol in line])

    legal_sequences = []

    for line in navigation_subsystem:

        legal_sequence = check_if_line_is_corrupt_and_return_legal_sequence(line)

        if legal_sequence is None:
            continue

        legal_sequences.append(legal_sequence)

    scores = compute_autocomplete_score(legal_sequences)
    middle_score = scores[int(len(scores)/2)]

    print(middle_score)

def compute_autocomplete_score(legal_sequences):
    symbols = {
        '' : 0,
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4
    }

    scores = []

    for sequence in legal_sequences:
        score = 0
        for symbol in sequence:
            score *= 5
            score += symbols[symbol]
        scores.append(score)

    return sorted(scores)

if __name__ == "__main__":
    part_one()
    part_two()
    