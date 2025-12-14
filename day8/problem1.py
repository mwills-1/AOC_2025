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

    def get_connected_components(self):
        visited = set()
        component_sizes = []
        
        for node in self.adj:
            if node not in visited:
                component_size = 0
                queue = deque([node])
                
                while queue:
                    current = queue.popleft()
                    if current in visited:
                        continue
                    
                    visited.add(current)
                    component_size += 1
                    
                    for neighbor in self.adj[current]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                
                component_sizes.append(component_size)
        
        return component_sizes

def parse_input(file_name):
    result = []
    with open(file_name) as f:
        for line in f:
            result.append(list(map(int, line.strip().split(","))))
    
    return result

def norm(v1, v2):
    assert len(v1) == len(v2)
    return sum((x - y) ** 2 for x, y in zip(v1, v2)) ** 0.5

def problem1(file_name, num_connections=1000):
    junctions = parse_input(file_name)
    g = Graph()

    for i in range(len(junctions)):
        g.add_node(i)

    norms = []
    for i, j1 in enumerate(junctions):
        for j, j2 in enumerate(junctions[i+1:]): 
            norms.append(((i, i + j + 1), norm(j1, j2)))
    norms.sort(key=lambda x: x[1])
    
    connections_made = 0
    for (j1, j2), dist in norms:
        g.add_edge(j1, j2)
        connections_made += 1
        if connections_made >= num_connections:
            break
        
    component_sizes = g.get_connected_components()
    component_sizes.sort(reverse=True)
    answer = component_sizes[0] * component_sizes[1] * component_sizes[2]
    
    return answer

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--file", "-f", help="Input File", required=True)
    parser.add_argument("--connections", "-c", type=int, default=10)
    args = parser.parse_args()

    p1 = problem1(args.file, args.connections)
    print(f"\nProblem1 {p1}")