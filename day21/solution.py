# STATUS: Answer too high but we can do a depth of 25

TRASLATION_KEY = {
    "0" : (3, 1), 
    "1" : (2, 0), 
    "2" : (2, 1), 
    "3" : (2, 2),
    "4" : (1, 0),
    "5" : (1, 1),
    "6" : (1, 2),
    "7" : (0, 0),
    "8" : (0, 1),
    "9" : (0, 2),
    "A" : (3, 2)
} 

TRASLATION_ARROW = {
    "^" : (0, 1),
    "A" : (0, 2),
    "<" : (1, 0),
    "v" : (1, 1),
    ">" : (1, 2)
}

def get_data (file): 
    results = []
    for line in file:
        results.append (line.strip())
    
    return results

def distance_m (a, b):
    return abs (a[0] - b[0]) + abs (a[1] - b[1])

def to_path (pos, target):
    prow, pcol = pos
    trow, tcol = target

    drow = prow - trow
    dcol = pcol - tcol 

    result = ""

    banned = (0,0)

    if banned == (prow - drow, pcol):
        if dcol > 0:
            result += "<" * dcol
        elif dcol < 0:
            result += ">" * abs (dcol)
        if drow > 0:
            result += "^" * drow
        elif drow < 0:
            result += "v" * abs (drow)
        
    else:
        if drow > 0:
            result += "^" * drow
        elif drow < 0:
            result += "v" * abs (drow)
        if dcol > 0:
            result += "<" * dcol
        elif dcol < 0:
            result += ">" * abs (dcol)
        
    result += "A"
    
    return result

# def direction_input (path, pos):
#     result = ""
#     for cmd in path:
#         # print (cmd)
#         pos_cords = TRASLATION_ARROW[pos]
#         target = TRASLATION_ARROW[cmd]
#         result += to_path (pos_cords, target)
#         pos = cmd

#     return result


# def second_robot (path, pos):
#     seqs = path.split ("A")
#     #print(seqs)
#     result = ""
#     for seq in seqs[:-1]:
#         pos_cords = TRASLATION_ARROW[pos]

#         ordered_seq = list (seq)
#         ordered_seq.sort (key = lambda cmd: -distance_m (TRASLATION_ARROW[cmd], pos_cords))
        
#         for cmd in ordered_seq:
#             target_cords = TRASLATION_ARROW[cmd]
#             pos_cords = TRASLATION_ARROW[pos]
            
#             to_add = to_path (pos_cords, target_cords)
#             result += to_add
#             pos = cmd
        
#         to_add = to_path (TRASLATION_ARROW[pos], TRASLATION_ARROW["A"])
#         result += to_add
#         pos = "A"
    
#     return result


def check_valid (symbols, pos, direction):
    if direction:
        cur = TRASLATION_ARROW[pos]
        banned = (0, 0)
    else:
        cur = TRASLATION_KEY[pos]
        banned = (3, 0)

    

    for cmd in symbols:
        row, col = cur

        if cmd == "<":
            cur = (row, col - 1)
        elif cmd == ">":
            cur = (row, col + 1)
        elif cmd == "v":
            cur = (row + 1, col)
        elif cmd == "^":
            cur = (row - 1, col)
        if cur == banned:
            return False
    return True

def direction_input (code, pos, direction = True):
    result = ""
    for sym in code:
        if direction:
            pos_cords = TRASLATION_ARROW[pos]
            target_cords = TRASLATION_ARROW[sym]
        else:
            pos_cords = TRASLATION_KEY[pos]
            target_cords = TRASLATION_KEY[sym]
    
        symbols = list (to_path (pos_cords, target_cords)[:-1])
        symbols.sort (key = lambda cmd: -distance_m (TRASLATION_ARROW[cmd], TRASLATION_ARROW["A"]))
    
        if not check_valid (symbols, pos, direction):
            symbols = symbols[::-1]
  
        result += "".join (symbols) + "A"
        pos = sym
        
    return result
        
def problem_1 (codes):
    sum = 0
    for code in codes:
        numeric = int (code[:-1])

        fpath = direction_input (code, "A", False)
        print(fpath)
        #print (len (fpath))
        spath = direction_input (fpath, "A")
        print(spath)
        #print (len (spath))
        tpath = direction_input (spath, "A")
        print(tpath)
        print (f"{code}: {len (tpath)}")
        # print (len (tpath), numeric)
        sum += len (tpath) * numeric
    
    return sum

def directional_keypad (path, pos, cache):
    result = ""

    for cmd in path:
        # print (cmd)
        pos_cords = TRASLATION_ARROW[pos]
        target = TRASLATION_ARROW[cmd]

        try:
            result += cache[(pos_cords, target)]
        except KeyError:
            cache[(pos_cords, target)] = to_path (pos_cords, target)
            result += cache[(pos_cords, target)]

        pos = cmd
    #print (cache)
    return result

# def problem_2 (codes):
#     sum = 0
    
#     for code in codes:
#         numeric = int (code[:-1])
#         path = direction_input (code, "A")
#         cache = {}
#         for _ in range (25):
#             print (_)
#             path = directional_keypad (path , "A", cache)

#         sum += len (path) * numeric
#     return sum

def level_down_direction (path, directional = True):
    result = ""
    if directional:
        flipped = {item: key for key, item in TRASLATION_ARROW.items ()}
        pos = TRASLATION_ARROW["A"]
    else: 
        flipped = {item: key for key, item in TRASLATION_KEY.items ()}
        pos = TRASLATION_KEY["A"]

    for cmd in path:

        row, col = pos
  
        if cmd == "<":
            pos = (row, col - 1)
        elif cmd == ">":
            pos = (row, col + 1)
        elif cmd == "v":
            pos = (row + 1, col)
        elif cmd == "^":
            pos = (row - 1, col)
        
        elif cmd == "A":
            result += flipped[pos]

    return result


def seq_directional_keypad (path, cache, dir_cache):
    result = ""
    seqs = path.split ("A")

    
    for seq in seqs[:-1]:
        seq += "A"

        try:
            result += cache[seq]
        except KeyError:
            new_cache = {}
            cache [seq] = directional_keypad (seq, "A", dir_cache)
            #print (cache)
            result += cache [seq]

    return result

def two_level (path, cache, seq_cache, last_cache):
    result = ""

    seqs = path.split ("A")

    for seq in seqs[:-1]:
        seq += "A"

        try:
            result += cache[seq]
        except KeyError:
            new_cache = {}
            cache [seq] = seq_directional_keypad (seq_directional_keypad (seq, seq_cache, last_cache), seq_cache, last_cache)
            #print (cache)
            result += cache [seq]

    return result

    
def break_path_up (path, num_threads):
    plist = path.split ("A")

    num_seq_per_thread = len (plist[-1]) // num_threads


    result = []
 

    for t in range (num_threads):
        result.append ("")
        for s in range (num_seq_per_thread):
            result[t] += plist [num_seq_per_thread * t + 1] + "A"
    
    return result



def cost_depth (path, depth):
    if path == "":
        return 0
    if depth == 0:
        return 0

    result = direction_input (path, "A")
    
    if depth == 1:
        #print (result, end = "")
        return len (result)
  
    # print (cache)
    seqs = result.split ("A")[:-1]

    return sum([cost_depth (seq + "A", depth - 1) for seq in seqs])


def build_up_cache (level = 10):
    result = {}
    seqs = ['<A', 'v<<A', 'v<A', '>>^A', 'vA', 'A', '<^A', '>A', '^>A', '^A', 'v>A', '>^A', '<vA']
    for seq in seqs:
        result[(seq, level)] = cost_depth (seq, level)

    return result

def hope (codes):
    cache = build_up_cache (level = 12)
    result = 0
    for code in codes:
        numeric = int (code[:-1])
        code_length = 0
        path = direction_input (code, "A", False)
        for _ in range (12):
            path = direction_input (path, "A")
        
        seqs = path.split ("A")[:-1]

        for seq in seqs:
            seq += "A"
            code_length += cache [(seq, 12)]
        
        print (f"{code} : {code_length}")
        result += code_length * numeric

    return result

# def problem_2 (codes):
#     cache = {}
#     for code in codes:
#         sum = 0
        
#         path = direction_input (code, "A")
#         seqs = path.split ("A")[:-1]
#         print (f"path: {path}")
#         for seq in seqs:
#             seq += "A"
#             #print (seq, cost_depth (seq, 1))
#             sum += cost_depth (seq, 20, cache)
    
#         print (f"{code}: {sum}")
#         break
#     return sum

if __name__ == "__main__":
    with open ("p21_input.txt", "r", encoding = "utf-8") as file:
        codes = get_data (file)

    #print (problem_1 (codes))
    #print (problem_2 (codes))
   # print (hope (codes))

    print (direction_input (direction_input (direction_input ("2A", "A", False), "A"), "A"))
    print (direction_input ("2A", "A", False))
    print (direction_input (direction_input ("<^A", "A"), "A"))
    print (direction_input (direction_input ("^<A", "A"), "A"))

    # cache = {}
    # seq_cache = {}
    # last_cache = {}
    # path = "029A"

    # path = direction_input (path, "A")
    # path = human_input (path, "A")

    # for _ in range (12):
    #     print (_)
    #     #print (path)
    #     path = two_level (path, cache, seq_cache, last_cache)


    # print (level_down_direction (level_down_direction ("<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A")))
    # print (level_down_direction ("<A>Av<<AA>^AA>AvAA^A<vAAA>^A"))
    # print (level_down_direction ("^A<<^^A>>AvvvA", directional = False))
    