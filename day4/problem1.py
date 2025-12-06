def parse_input(file_name):
    rolls = []
    with open(file_name) as file:
        for line in file:
            rolls.append(list(line.strip()))
    return rolls

def build_graph(rolls):
    num_rolls = len(rolls)
    roll_len = len(rolls[0])
    
    # 8 directions: up, down, left, right, and 4 diagonals
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    accessible_count = 0
    
    for i in range(num_rolls):
        for j in range(roll_len):
            if rolls[i][j] == '@':
                adjacent_rolls = 0
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < num_rolls and 0 <= nj < roll_len:
                        if rolls[ni][nj] == '@':
                            adjacent_rolls += 1
                
                if adjacent_rolls < 4:
                    accessible_count += 1
    
    return accessible_count

if __name__ == '__main__':
    rolls = parse_input('input.txt')
    result = build_graph(rolls)
    print(f"Number of accessible rolls: {result}")