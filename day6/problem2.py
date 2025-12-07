import operator
from functools import reduce
ops = {
    "*": (operator.mul, 1),
    "+": (operator.add, 0),
}

class Expression:
    def __init__(self):
        self.numbers = []
        self.op = None

    def add_number(self, number):
        self.numbers.append(number)
    
    def add_op(self, op):
        self.op = op
    
    def eval(self):
        operator, start = ops[self.op]
        return reduce(operator, self.numbers, start)

def problem2(file_name):
    problems = []
    with open(file_name) as f:
        for line in f:
            problems.append(list(line))
    
    num_rows = len(problems)
    num_cols = len(problems[0])
    total = 0
    curr_problem = Expression()
    for col in range(num_cols):
        seperator_col = True
        number = ''
        for row in range(num_rows):
            try:
                val = problems[row][col]
            except IndexError:
                val = " "

            if val == " ":
                continue
            if val.isdigit():
                seperator_col = False
                number += val
            if val in ['*', '+']:
                seperator_col = False
                curr_problem.add_op(val)
            
        if seperator_col:
            total += curr_problem.eval()
            curr_problem = Expression()
        else:
            curr_problem.add_number(int(number))

    return total
            
if __name__ == "__main__":
    p2 = problem2('input.txt')
    print(f"Problem 2 {p2}")