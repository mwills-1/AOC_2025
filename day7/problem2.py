import numpy as np
from argparse import ArgumentParser
from collections import deque


class QuantumBeams():
    def __init__(self):
        self.beams = deque()
        self.num_beams = {}
    
    def add_beam(self, location, num_beams):
        if location in self.num_beams:
            self.num_beams[location] += num_beams
        else:
            self.beams.append(location)
            self.num_beams[location] = num_beams
    
    def get_beam(self):
        beam = self.beams.popleft()
        num_beams = self.num_beams[beam]
        return beam, num_beams


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


def problem2(verbose):
    board, start_beam = parse_input('input.txt')
    qbeams = QuantumBeams()
    qbeams.add_beam(start_beam, 1)

    num_rows = len(board) 
    num_cols = len(board[0])
    
    visited = {} 
    
    while qbeams.beams:
        (row, col), num_beams = qbeams.get_beam()
        
        if (row, col) in visited:
            continue
        visited[(row, col)] = num_beams

        if row + 1 < num_rows and board[row + 1][col] == '^':
            if verbose:
                if col + 1 < num_cols:
                    board[row + 1][col + 1] = f'{num_beams}'
                if col - 1 >= 0:
                    board[row + 1][col - 1] = f'{num_beams}'
            
            if col + 1 < num_cols:
                qbeams.add_beam((row + 1, col + 1), num_beams)
            if col - 1 >= 0:
                qbeams.add_beam((row + 1, col - 1), num_beams)   
        else:
            if row + 1 < num_rows:
                if verbose:
                    board[row + 1][col] = f'{num_beams}'
                qbeams.add_beam((row + 1, col), num_beams)   
        
        if verbose:  
            print_board(board)
            print()
    
    timelines = 0
    for (row, col), value in visited.items():
        if row == num_rows - 1:
            timelines += value
    
    return timelines


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()

    p2 = problem2(args.verbose)
    print(f"Problem2 {p2}")