import operator

ops = {
    "*": (operator.mul, 1),
    "+": (operator.add, 0),
}

def parse_input(file_name):
    problems = []
    with open(file_name) as f:
        for line in f:
            problems.append(line.strip().split())
    
    return [list(map(int, lst)) for lst in problems[:-1]], problems[-1]

def problem1():
    problems, operators = parse_input(f'input.txt')

    num_problems = len(problems)
    num_numbers = len(problems[0])
    total = 0
    
    for col in range(num_numbers):
        op, result = ops[operators[col]]
        for row in range(num_problems):
            result = op(result, problems[row][col])
        total += result
    
    return total

            
if __name__ == "__main__":
    p1 = problem1()
    print(f"Problem 1 {p1}")