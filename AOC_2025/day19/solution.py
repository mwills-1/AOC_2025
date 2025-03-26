
def get_data (file):
    combos = []
    towels = []
    for i, line in enumerate (file):
        if i == 0:
            split_combos = line.strip().split(",")
            for c in split_combos:
                combos.append(c.strip())
        elif i == 1:
            continue
        else:
            towels.append(line.strip())

    return combos, towels
def check_valid (combos, towel_part):
    #print(towel_part)
    if towel_part == "":
        return True
    
    valid_c = []
    for combo in combos:
        if towel_part.find(combo) == 0:
            valid_c.append (combo)
    
    if len (valid_c) == 0:
        return False
    
    for c in valid_c:
        if check_valid (combos, towel_part [len(c):]):
            return True
    
    return False

def count_valid (combos, towel_part, cache):
    if towel_part == "":
        return 1
    
    valid_c = []
    for combo in combos:
        if towel_part.find(combo) == 0:
            valid_c.append (combo)
    
    if len (valid_c) == 0:
        return 0
    
    sum = 0
    
    for c in valid_c:
        next = towel_part[len(c):]
        try:
            sum += cache[next]
        except KeyError:
            cache[next] = count_valid (combos, next, cache)
            sum += cache[next]

    return sum


if __name__ == "__main__":
    with open ("p19_input.txt", "r", encoding = "utf-8") as file:
        combos, towels = get_data (file)

    print(combos)
    print(towels)

    sum = 0
    for towel in towels:
        if check_valid (combos, towel):
            sum += 1
    print(sum)

    sum = 0
    cache = {}
    for towel in towels:
        sum += count_valid (combos, towel, cache)
    print(sum)
