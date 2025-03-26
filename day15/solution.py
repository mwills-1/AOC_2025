

def get_data (file):
    board = []
    moves = ""
    start_loc = -1
    count = 0
    for y, line in enumerate(file):
        line = line.strip()
       
        if count <= 1:
            board.append(list(line))
        else:
            moves += line
        
        if line.count ("#") == len(line):
            count += 1

        for x, char in enumerate(line):
            if char == "@":
                start_loc = (x,y)
    
    return board, moves, start_loc

def update_board (board, move, bot_loc):
    x, y = bot_loc
    i = 1
    if move == "<":
        while True:
            if board[y][x - i] == "#":
                return (x, y)
                
            elif board[y][x - i] == ".":
                board[y][x - i] = "O"
                board[y][x - 1] = "@"
                board[y][x] = "."
                break
            i += 1
        return (x - 1,y)

    elif move == ">":
        while True:
            if board[y][x + i] == "#":
                return (x, y)
            elif board[y][x + i] == ".":
                board[y][x + i] = "O"
                board[y][x + 1] = "@"
                board[y][x] = "."
                break
            i += 1
        return (x + 1, y)
    
    elif move == "^":
        while True:
            if board[y - i][x] == "#":
                return (x, y)
            elif board[y - i][x] == ".":
                board[y - i][x] = "O"
                board[y - 1][x] = "@"
                board[y][x] = "."
                break
            i += 1
        return (x, y - 1)
    
    elif move == "v":
        while True:
            if board[y + i][x] == "#":
                return (x, y)
            elif board[y + i][x] == ".":
                board[y + i][x] = "O"
                board[y + 1][x] = "@"
                board[y][x] = "."
                break
            i += 1
        
        return (x, y + 1)

def run_moves(board, moves, bot_loc, p = False):
    new_bot_loc = bot_loc
    count = 0

    if p: 
        print("Initial State:")
        print_board (board)
    for i, move in enumerate (moves):
        new_bot_loc = update_board (board, move, new_bot_loc)
        if p: 
            print(f"After {i + 1} moves {move}:")
            print_board (board)

def print_board (board):
    for line in board:
        for char in line:
            print (char, end = "")
        print ()
    print ()
    
def calc_board_score (board):
    score = 0
    for i, line in enumerate (board): 
        for j, char in enumerate(line):
            if char  == "O":
                score += 100 * i + j
    return score

def problem_2_make_board(board):
    new_board = []
    temp = ""
    start_loc = -1
    for i, line in enumerate (board):
        for j, char in enumerate(line):
            if char == "@":
                temp += "@."
                start_loc = (j * 2, i)
            elif char == "O":
                temp += "[]"
            else:
                temp += char * 2
        new_board.append(list(temp))
        temp = ""
    
    return new_board, start_loc


def problem_2_update_board (board, move, bot_loc):
    x, y = bot_loc
    i = 1
    def write_boxes (board, start, end):
        sx, sy = start
        ex, ey = end
        
        for y in range (sy, ey):
            for x in range(sx, ex):
                if (x-sx) % 2== 0:
                    board[y][x] = "["
                else:
                    board[y][x] = "]"
            if (y-sy) % 2== 0:
                board[y][x] = "["
            else:
                board[y][x] = "]"
            
    if move == "<":
        while True:
            if board[y][x - i] == "#":
                return (x, y)
                
            elif board[y][x - i] == ".":
                write_boxes (board, (x-i, y), (x, y+1))
                board[y][x - 1] = "@"
                board[y][x] = "."
                break
            i += 1
        return (x - 1,y)

    elif move == ">":
        while True:
            if board[y][x + i] == "#":
                return (x, y)
            elif board[y][x + i] == ".":
                write_boxes (board, (x+2, y), (x+i+1, y))
                board[y][x + 1] = "@"
                board[y][x] = "."
                break
            i += 1
        return (x + 1, y)
    
    elif move == "^":
        while True:
            if board[y - i][x] == "#":
                return (x, y)
            elif board[y - i][x] == ".":
                write_boxes (board, (x,y-i), (x,y-1))
                board[y - 1][x] = "@"
                board[y][x] = "."
                break
            i += 1
        return (x, y - 1)
    
    elif move == "v":
        while True:
            if board[y + i][x] == "#":
                return (x, y)
            elif board[y + i][x] == ".":
                write_boxes (board, (x, y+1), (x, y + i))
                board[y + 1][x] = "@"
                board[y][x] = "."
                break
            i += 1
        
        return (x, y + 1)


def problem_2_run_moves(board, moves, bot_loc, p = False):
    new_bot_loc = bot_loc
    count = 0

    if p: 
        print("Initial State:")
        print_board (board)
    for i, move in enumerate (moves):
        new_bot_loc = problem_2_update_board (board, move, new_bot_loc)
        if p: 
            print(f"After {i + 1} moves {move}:")
            print_board (board)
            if i == 2:
                break
    


if __name__ == "__main__":
    with open ("test_input.txt", "r", encoding ="utf-8") as file:
        data = get_data (file)

    #print (data)
    p2_board, p2_loc= problem_2_make_board (data[0])
    print(p2_board, p2_loc)
    problem_2_run_moves (p2_board, data[1], p2_loc, p=True)
    run_moves (data[0], data[1], data[2])
    

    score = calc_board_score(data[0])
    #print(score)



