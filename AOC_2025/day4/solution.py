import numpy as np

def get_data(file):
    res = []
    for line in file:
        res.append(np.array(list(line.strip())))
    
    return np.array(res)


def search_xmas(row, col, input):
    n = input.shape[0]
    left_idx = max(row-4, 0)
    right_idx = min(row+4, n)

    top_idx = max(col-4, 0)
    bottom_idx = min(col+4, n)

    print(left_idx)
    print(right_idx)
    print(top_idx)
    print(bottom_idx)

    print(input[left_idx:right_idx, top_idx:bottom_idx])




def find_xmas(input):

    for i, row in enumerate(input):
        for j, letter in enumerate(row):
            if letter == "X":
                search_xmas(i, j, input)


if __name__ == "__main__":
    with open("p4_input.txt") as file:
        data = get_data(file)
    # print(data.shape)
    # print(data)

    search_xmas(50, 50, data)