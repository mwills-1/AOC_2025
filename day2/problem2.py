
def parse_input(file_name):
    with open(file_name) as f:
        res = f.read().strip().split(',')
    return res

def problem2():
    ids = parse_input('input.txt')
    sum = 0
    for id in ids:
        start_id, end_id = list(map(int, id.split('-')))
        for sub_id in range(start_id, end_id+1):
            sub_id = str(sub_id)
            length = len(sub_id)
            for i in range(1, length):
                if length % i == 0 and sub_id == sub_id[:i] * (length // i):
                    sum += int(sub_id)
                    break
    return sum

if __name__ == '__main__':
    p2 = problem2()
    print(f'Problem 2 {p2}')