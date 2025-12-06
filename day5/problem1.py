
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


def problem1():
    intervals, numbers = parse_file('input.txt')
    fresh = 0
    for number in numbers:
        for start, end in intervals:
            if start <= number <= end:
                fresh += 1
                break
            
    return fresh

if __name__ == '__main__':
    p1 = problem1()
    print(f"Problem1 {p1}")