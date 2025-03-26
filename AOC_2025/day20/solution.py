import math
from pprint import pprint

def get_data (file):
    maze = []
    start = (0,0)
    end = (0,0)
    for row, line in enumerate (file):
        to_append = list(line.strip()[1:-1])
        for col, char in enumerate (to_append):
            if char == "S":
                start = (row-1, col)
            if char == "E":
                end = (row-1, col)
        
        maze.append(to_append)

    del maze[0]
    del maze[-1]

    return maze, start, end

def print_maze (maze):
    result = ""
    for row in maze:
        for char in row:
            result += char
        result += "\n"

    print(result)

def get_neighbors (maze, vertex, SIZE):
    row, col = vertex
    result = []

    left_index = row - 1
    right_index = row + 1
    up_index = col - 1
    down_index = col + 1
    
    if left_index >= 0 and maze[left_index][col] != "#":
        result.append(((left_index, col)))
    if right_index <= SIZE and maze[right_index][col] != "#":
        result.append(((right_index, col)))
    if up_index >= 0 and maze[row][up_index] != "#":
        result.append(((row, up_index)))
    if down_index <= SIZE and maze[row][down_index] != "#":
        result.append((row, down_index))
    
    return result



def get_min_unvisited (unvisited, distance):
    min_dist = distance[unvisited[0]]
    min_v = unvisited[0]
    for v in unvisited:
        if distance [v] < min_dist:
            min_dist = distance[v]
            min_v = v

    return min_v

def dijkstras (maze, start, SIZE):
    distances = {}
    unvisited = []

    for row in range (SIZE + 1):
        for col in range (SIZE + 1):
            if maze[row][col] != "#":
                unvisited.append((row, col))
                distances[(row, col)] = float('inf')

    distances[start] = 0
    while unvisited:
        v = get_min_unvisited (unvisited, distances)
        dist = distances[v]

        if math.isinf (dist):
            break

        unvisited.remove(v)
        
        neighbors = get_neighbors (maze, v, SIZE)

        for n in neighbors:
            if dist + 1 < distances[n]:
                distances[n] = dist + 1
    return distances

def get_shortcuts (v, SIZE):
    row, col = v
    result = []

    right_index = row + 2
    down_index = col + 2
    
    if right_index <= SIZE:
        result.append(((right_index - 1, col), (right_index, col)))
  
    if down_index <= SIZE:
        result.append(((row, down_index - 1), (row, down_index)))
    
    return result

def get_all_neighbors (v, SIZE):
    row, col = v
    result = []

    left_index = row - 1
    right_index = row + 1
    up_index = col - 1
    down_index = col + 1
    
    if left_index >= 0:
        result.append(((left_index, col)))
    if right_index <= SIZE:
        result.append(((right_index, col)))
    if up_index >= 0:
        result.append(((row, up_index)))
    if down_index <= SIZE:
        result.append((row, down_index))
    
    return result


def time_save_compute (shortcut, distances, SIZE):
    first, second = shortcut

    if second not in distances.keys():
        return -1
    # n1 = get_all_neighbors (first, SIZE)
    # n2 = get_all_neighbors (second, SIZE)

    

    # max_time_save = -1
    # for n_1 in n1:
    #     if n_1 in distances.keys ():
    #         for n_2 in n2:
    #             if n_2 in distances.keys ():
    #                 row1, col1 = n_1
    #                 row2, col2 = n_2
    #                 length_of_shortcut = abs(row1 - row2) + abs(col1 - col2)
    #                 saved = abs (distances[n_1] - distances[n_2]) - length_of_shortcut
    #                 if saved > max_time_save:
    #                     max_time_save = saved
    length_of_shortcut = abs(first[0] - second[0]) + abs(first[1] - second[1])
    return abs (distances[first] - distances[second]) - length_of_shortcut

def problem_1 (maze, start, SIZE):

    distances = dijkstras (maze, start, SIZE)

    time_save_dict = {}
    for point in distances.keys ():
        #print (point)
        surrounding = get_surrounding (distances, point, 2)
        for s in surrounding:
            if (s, point) not in time_save_dict.keys ():
                time_save_dict[(point, s)] = time_save_compute ((point, s), distances, SIZE)


    # distances = dijkstras (maze, start, SIZE)
    # time_saved_dict = {}
    # for row in range (SIZE + 1):
    #     for col in range (SIZE + 1):
    #         short_cuts = get_shortcuts((row, col), SIZE)
    #         for short_cut in short_cuts:
    #             time_saved = time_save_compute (short_cut, distances, SIZE)
    #             time_saved_dict[short_cut] = time_saved

    pprint(time_save_dict)
    count = 0
    for val in time_save_dict.values ():
        if val >= 100:
            count += 1

    return count


def get_surrounding (distances, point, max_distance):
    row, col = point
    points = []

    for drow in range(-max_distance, max_distance + 1):
        dcol_limit = max_distance - abs(drow)
        for dcol in range(-dcol_limit, dcol_limit + 1):
            if (row + drow, col + dcol) in distances.keys():
                points.append((row + drow, col + dcol))

    return points

def remove_dups(dict):
    to_remove = []
    for tup in dict:
        tup1, tup2 = tup
        if (tup2, tup1) in dict.keys ():
            to_remove.append((tup2, tup1))
    
    for remove in to_remove:
        del dict[remove]

def problem_2 (maze, start, SIZE):
    distances = dijkstras (maze, start, SIZE)

    time_save_dict = {}
    for point in distances.keys ():
        surrounding = get_surrounding (distances, point, 20)

        for s in surrounding:
            if (s, point) not in time_save_dict.keys ():
                time_save_dict[(point, s)] = time_save_compute ((point, s), distances, SIZE)
           

    # pprint(time_save_dict)
    count = 0
    for val in time_save_dict.values ():
        if val >= 100:
            count += 1

    return count

            
if __name__ == "__main__":
    with open ("p20_input.txt") as file:
        maze, start, end = get_data(file)

    #print_maze (maze)
    #print(start, end)

    SIZE = len(maze[0]) - 1
    #pprint(problem_1 (maze, start, SIZE))
    #print_maze (maze)
    print (problem_2 (maze, start, SIZE))
