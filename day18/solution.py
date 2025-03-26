from graph import Graph
SIZE = 70

def get_data (file):
    board = []
    for _ in range (SIZE + 1):
        board.append(["."] * (SIZE + 1))
    
    c_mem = []
    for line in file:

        c_mem.append (list (map (int, line.strip().split(","))))
    
    return board, c_mem

def print_maze (board):
    result = ""
    for row in board:
        for char in row:
            result += char
        result += "\n"
    print(result)


def do_corrupt_mem (maze, corr_mem, num_mem_corpt):

    for i, mem in enumerate (corr_mem):
        if i == num_mem_corpt:
            break
        x, y = mem
        maze[y][x] = "#"

def maze_to_graph (maze):
    g = Graph ()
    for r, row in enumerate(maze):
        for c, char in enumerate(row):
            #print(char)
            if char != "#":
                g.add_node (f"({r}, {c})", (r, c))
    
    for v in g.vertices:
        row, col = v.location
        v_left = g.find_vertice (f"({row-1}, {col})")
        v_right = g.find_vertice (f"({row+1}, {col})")
        v_up = g.find_vertice (f"({row}, {col-1})")
        v_down = g.find_vertice (f"({row}, {col+1})")

        if v_left != -1:
            g.add_edge (v, v_left)
        if v_right != -1:
            g.add_edge (v, v_right)
        if v_up != -1:
            g.add_edge (v, v_up)
        if v_down != -1:
            g.add_edge (v, v_down)
    return g

def find_samllest_unvisited (unvisited):
    min_distance = None
    min_vertex = None

    for ver in unvisited:
        if ver.distance > -1 and (min_distance is None or ver.distance < min_distance):
            min_distance = ver.distance 
            min_vertex = ver
    
    return min_vertex if min_vertex is not None else None


def dijkstra (graph, start, finish):
    unvisited = graph.vertices.copy()

    current = start
    current.distance = 0

    while True:
        if current == finish:
            break
        for neighbor in current.neighbors:
            if neighbor.distance == -1:
                neighbor.distance = current.distance + 1
            elif neighbor.distance > current.distance + 1:
                neighbor.distance = current.distance + 1

        unvisited.remove(current)
        current = find_samllest_unvisited (unvisited)
        
        if current is None:
            break


def add_neighbors (maze, vertex):
    row, col = vertex[0]
    dist = vertex[1]
    result = []

    left_index = max(row -1, 0)
    right_index = min(row + 1, SIZE)
    up_index = max (col - 1, 0)
    down_index = min (col + 1, SIZE)
    
    if maze[left_index][col] != "#":
        result.append(((left_index, col), dist + 1))
    if maze[right_index][col] != "#":
        result.append(((right_index, col), dist + 1))
    if maze[row][up_index] != "#":
        result.append(((row, up_index), dist + 1))
    if maze[row][down_index] != "#":
        result.append(((row, down_index), dist + 1))
    
    return result


def easier_dijkstas (maze, start, finish):
    visited = set()
    queue = [(start, 0)]

    current_distance = 0

    while queue:
        current = queue.pop (0)
        location, distance = current

        if location == finish:
            return distance

        if location not in visited:
            queue += add_neighbors (maze, current)
            visited.add(location)
        
    return -1



def problem_2 (maze, mem):
    start = (0,0)
    finish = (SIZE, SIZE)
    for corrupted in range (1024, 3451):
        do_corrupt_mem (maze, mem, corrupted)
        print(corrupted)
        if easier_dijkstas (maze, start, finish) == -1:
            return corrupted

    return -1
    

if __name__ == "__main__":
    
    with open ("p18_input.txt", "r", encoding = "utf-8") as file:
        maze, mem = get_data (file)

    final_index = problem_2 (maze, mem)
    print(final_index)

    # do_corrupt_mem (maze, mem, 1024)
    # result = easier_dijkstas (maze, (0,0), (SIZE, SIZE))

    # print(result)

    #final_index = problem_2 (maze, mem)
    # print (final_index)
    #print_maze(maze)
    # do_corrupt_mem (maze, mem, 1024)
    # graph = maze_to_graph (maze)
    #print_maze(maze)

    # for v in graph.vertices:
    #     print(v.name, end = " [")
    #     for n in v.neighbors:
    #         print(n, end = " ")
    #     print("]")
    
    # s = graph.find_vertice ("(0, 0)")
    # f = graph.find_vertice (f"({str(SIZE)}, {str(SIZE)})")

    # dijkstra (graph, s, f)
    # print(f.distance)