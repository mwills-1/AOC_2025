def parse_file(file_name):
    intervals = []
    numbers = []
    with open(file_name) as file:
        for line in file:
            s_line = line.strip()
            if "-" in line:
                intervals.append(tuple(map(int, s_line.split('-'))))
            elif s_line != '':
                numbers.append(int(s_line))
    return intervals, numbers

def problem2():
    intervals, _ = parse_file('input.txt')

    intervals.sort()
    
    overlapping = []
    for start, end in intervals:
        if overlapping == []:
            overlapping.append([start, end])
            continue
        oend = overlapping[-1][1]

        if start > oend:
            overlapping.append([start, end]) 
        
        elif end > oend:
            overlapping[-1][1] = end

    return sum(map(lambda interval: interval[1] - interval[0] + 1, overlapping))

if __name__ == '__main__':
    p2 = problem2()

    print(f"Problem2 {p2}")