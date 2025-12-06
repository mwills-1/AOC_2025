def parse_input(file_name):
    rolls = []
    with open(file_name) as file:
        for line in file:
            rolls.append(list(line.strip()))
    return rolls

def count_adjacent_rolls(rolls, i, j):
    num_rolls = len(rolls)
    roll_len = len(rolls[0])
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    adjacent_count = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < num_rolls and 0 <= nj < roll_len:
            if rolls[ni][nj] == '@':
                adjacent_count += 1
    
    return adjacent_count

def find_accessible_rolls(rolls):
    num_rolls = len(rolls)
    roll_len = len(rolls[0])
    
    accessible = []
    
    for i in range(num_rolls):
        for j in range(roll_len):
            if rolls[i][j] == '@':
                if count_adjacent_rolls(rolls, i, j) < 4:
                    accessible.append((i, j))
    
    return accessible

def remove_rolls(rolls):
    total_removed = 0
    
    while True:
        accessible = find_accessible_rolls(rolls)
        
        if not accessible:
            break
        
        for i, j in accessible:
            rolls[i][j] = '.'
        
        total_removed += len(accessible)
        print(f"Removed {len(accessible)} rolls (total: {total_removed})")
    
    return total_removed

if __name__ == '__main__':
    rolls = parse_input('input.txt')
    result = remove_rolls(rolls)
    print(f"\nTotal rolls removed: {result}")