from argparse import ArgumentParser
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.edges_added = 0
    
    def add_node(self, v):
        self.adj[v]

    def add_edge(self, v, u):
        if self.creates_cycle(v, u):
            return -1
        else:
            self.adj[v].append(u)
            self.adj[u].append(v)
            self.edges_added += 1
            return 0

    def creates_cycle(self, v, u):
        if v == u:
            return True
        queue = deque([v])
        visited = set([v])
        
        while queue:
            node = queue.popleft()
            
            for neighbor in self.adj[node]:
                if neighbor == u:
                    return True  
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False

def parse_input(file_name):
    result = []
    with open(file_name) as f:
        for line in f:
            result.append(list(map(int, line.strip().split(","))))
    
    return result

def norm(v1, v2):
    assert len(v1) == len(v2)
    return sum((x - y) ** 2 for x, y in zip(v1, v2)) ** 0.5

def problem1(file_name):
    junctions = parse_input(file_name)
    g = Graph()

    for i in range(len(junctions)):
        g.add_node(i)

    norms = []
    for i, j1 in enumerate(junctions):
        for j, j2 in enumerate(junctions[i+1:]): 
            norms.append(((i, i + j + 1), norm(j1, j2)))
    norms.sort(key=lambda x: x[1])
    
    result = -1
    connections_made = 0
    for (j1, j2), _ in norms:
        g.add_edge(j1, j2)
        connections_made += 1

        if g.edges_added == (len(g.adj) - 1):
            result = junctions[j1][0] * junctions[j2][0]
            break
    
    return result

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--file", "-f", help="Input File", required=True)
    args = parser.parse_args()

    p1 = problem1(args.file)
    print(f"Problem1 {p1}")