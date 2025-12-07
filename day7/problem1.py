import numpy as np
from argparse import ArgumentParser

def parse_input(file_name):
    board = []
    beam_start = None
    with open(file_name) as f:
        for i, line in enumerate(f):
            if 'S' in line:
                beam_start = i, line.find('S')
            board.append(list(line.strip()))
    
    return np.array(board), beam_start


def print_board(board):
    for row in board:
        print("".join(row))


def problem1(verbose):
    board, start_beam = parse_input('input.txt')
    beam_locations = [start_beam]

    num_rows = len(board) 
    num_cols = len(board[0])
    
    visited = set()
    split = 0
    while beam_locations:
        row, col = beam_locations.pop()

        if (row, col) in visited:
            continue
        visited.add((row, col))

        if row + 1 < num_rows and board[row + 1][col] == '^':
            if verbose:
                board[row + 1][col + 1] = '|'
                board[row + 1][col - 1] = '|'
            if col < num_cols:
                beam_locations.append((row + 1, col + 1))
            if col >= 0:
                beam_locations.append((row + 1, col - 1))   
            split += 1 
        else:
            if row + 1 < num_rows:
                if verbose:
                    board[row + 1][col] = '|'
                beam_locations.append((row + 1, col))   
        if verbose:  
            print_board(board)

    return split
    


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()

    p1 = problem1(args.verbose)
    print(f"Problem1 {p1}")