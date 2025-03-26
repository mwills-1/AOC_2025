
HEIGHT = 103
WIDTH = 101

def get_data (file):

    result = {}
    for i, line in enumerate(file):
        line = line.strip ()
        p, v = line.split (" ")
        px, py = p[2:].split (",")
        vx, vy = v[2:].split (",")
        
        px = int(px)
        py = int(py)
        vx = int(vx)
        vy = int(vy)
        result["bot" + str(i)] = {"p" : (px, py), "v" : (vx, vy)}

    return result

def calc_position (start_pos, velo, time):

    #calc the new x postion moding by number of tiles
    new_x = (start_pos[0] + (velo[0] * time)) % WIDTH

    #same as above
    new_y = (start_pos[1] + (velo[1] * time)) % HEIGHT
    return [new_x, new_y]

def make_string_board (bot_data, time, height, width):
    positions = {}
    result = ""
    for bot in bot_data.values ():
        pos = calc_position (bot["p"], bot["v"], time)
        key = str(pos[0]) + "," + str(pos[1])
        positions[key] = positions.get (key, []) + [pos]

    for h in range(height):
        for w in range(width):
            key = str(w) + "," + str(h)

            length = len (positions.get (key, []))
            if length == 0:
                result += "."
            else:
                result += str(length)
        result += "\n"
    return result

def print_board (bot_data, time, height, width):
    """
    Prints the position of the board at time time. 
    """
    print(make_string_board (bot_data, time, height, width))

def calc_safety_score (bot_data, time, height, width): 
    """
    Calculates the safety score at time t
    """

    board = make_string_board (bot_data, time, height, width).strip()
    board_matrix = board.split ('\n')
    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0
    # print(height // 2)
    # print(width // 2)
    for h in range(height // 2):
        for w in range(width // 2):
            peice = board_matrix[h][w]
            quad1 += 0 if peice == "." else int(peice)

            peice = board_matrix[h][(width // 2) + w + 1]
            quad2 += 0 if peice == "." else int(peice)

            peice = board_matrix[(height //2) +h + 1][w]
            quad3 += 0 if peice == "." else int(peice)

            peice =  board_matrix[(height // 2) + h + 1][(width // 2) + w + 1]
            quad4 += 0 if peice == "." else int(peice)
    
    # print(quad1)
    # print(quad2)
    # print(quad3)
    # print(quad4)

    return quad1 * quad2 * quad3 * quad4

def check_rows (string):
    in_a_row = 0
    string_m = string.strip().split("\n")
    for row in string_m:
        for char in row:
            if char ==".":
                in_a_row = 0
            else:
                in_a_row += 1
            if in_a_row >= 5:
                return True
            
    return False
        

def find_easter_egg(data):
    for t in range(1, 10000):
        board = make_string_board(data, t, HEIGHT, WIDTH)
        if check_rows (board):
            print(f"After {t} seconds:")
            print(board)

if __name__ == "__main__":
    with open("p14_input.txt","r", encoding = "utf-8") as file:
        data = get_data (file)
    
    #print (data)
    #print_board(data, 100,7,11)
    ss = calc_safety_score (data, 100, HEIGHT, WIDTH)
    print(ss)
    
    find_easter_egg(data)