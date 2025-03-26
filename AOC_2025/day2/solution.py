from itertools import pairwise
def get_data(file):
    res = []
    for line in file:
        res.append([int (x) for x in line.strip().split(" ")])
    
    return res

def safe(report):
    increasing = all (a < b for a, b in pairwise(report))
    decreasing = all (a > b for a, b in pairwise(report))
    distance = all (0 < abs(a - b) < 4 for a, b in pairwise(report))

    return (increasing or decreasing) and distance

def safeness(input):
    num_safe = 0
    for report in input:
        if safe(report):
            num_safe += 1
    
    return num_safe

def damping(input):
    num_safe = 0
    for report in input:
        if safe(report):
            num_safe += 1
        else:
            length = len(report)
            for i in range(length):
                new_report = report[:i] + report[i+1:]
                if safe(new_report):
                    num_safe += 1
                    break
    return num_safe


if __name__ == "__main__":
    with open("p2_input.txt") as file:
        data = get_data(file)

    result = safeness(data)
    print(result)

    result2 = damping(data)
    print(result2)
