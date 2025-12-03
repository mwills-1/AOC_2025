def parse_input(file_name):
    moves = []
    with open(file_name) as file:
        for line in file:
            moves.append(line.strip())
    return moves

def problem1():
    moves = parse_input('input1.txt')
    position = 50
    count = 0
    for move in moves:
        direction = move[0]
        turns = int(move[1:])

        if direction == 'L':
            position -= turns
        elif direction == 'R':
            position += turns
        position = position % 100
        
        if position == 0:
            count += 1
       
    return count

def problem2():
    moves = parse_input('input1.txt')

    position = 50          # current dial position (0–99)
    count = 0              # number of times we cross 0

    for move in moves:
        direction = move[0]
        amount = int(move[1:])

        step = -1 if direction == 'L' else 1

        for _ in range(amount):
            prev = position
            position = (position + step) % 100

            # Count ONLY if we passed through 0
            if position == 0:
                count += 1

    return count
   

if __name__ == "__main__":
    p1 = problem1()
    p2 = problem2()
    print(f"Problem 1: {p1}")
    print(f'Problem 2: {p2}')