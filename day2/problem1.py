
def parse_input(file_name):
    with open(file_name) as f:
        res = f.read().strip.split(',')
    return res

def problem1():
    ids = parse_input('input.txt')
    sum = 0
    for id in ids:
        start_id, end_id = list(map(int, id.split('-')))
        for sub_id in range(start_id, end_id+1):
            sub_id = str(sub_id)
            length = len(sub_id)
            if length % 2 == 1:
                continue
            mid = length // 2
            if sub_id[:mid] == sub_id[mid:]:
                sum += int(sub_id)
    return sum

if __name__ == '__main__':
    p1 = problem1()
    print(f'Problem 1 {p1}')