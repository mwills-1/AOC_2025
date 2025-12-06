
def parse_file(file_name):
    result = []
    with open(file_name) as file:
        for line in file:
            result.append(line.strip())
    return result


def problem1():
    batteries = parse_file('input.txt')
    sum = 0
    for row in batteries:
        left = 0
        right = 1
        num = -1
        while right < len(row):
            if num < int(row[left] + row[right]):
                num = int(row[left] + row[right])
            if row[left] < row[right]:
                left = right
            right += 1
        sum += num
            
    return sum


if __name__ == '__main__':
    p1 = problem1()
    print(f'Problem 1 {p1}')