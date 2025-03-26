from graph import Graph, Vertex
import numpy as np
import matplotlib.pyplot as plt

NAME = "start"

def location_check (loc1, loc2):
    """
    Checks if the values of two tuples are the same
    """
    return loc1[0] == loc2[0] and loc1[1] == loc2[1]

def location_update (loc, up):
    return (loc[0]+ up [0], loc[1] + up[1])
def name_update():
    global NAME

    if NAME == "start":
        NAME = "1"
    else:
        NAME = str(int(NAME) + 1)


def make_graph_helper (g, A, B, start_node, prize_location):
    if start_node.norm() > np.linalg.norm(prize_location):
        return
    if location_check (start_node.location, prize_location):
        return
    
    a = Vertex (NAME, location_update (start_node.location, A))
    name_update ()
    b = Vertex (NAME, location_update (start_node.location, B))
    name_update ()
    
    g.add_edge (start_node, a)
    g.add_edge (start_node, b)

    make_graph_helper (g, A, B, a, prize_location)
    make_graph_helper (g, A, B, b, prize_location)

    

def make_graph (A, B, prize):
    g = Graph ()
    start_n = Vertex (NAME, (0,0))
    name_update ()
    g.add_vertex (start_n)
    
    make_graph_helper (g, A, B, start_n, prize)
    return g

def plot_graph (g):
    data = []
    for v in g.vertices:
        print(v.name)
        data.append(v.location)
    x, y = zip(*data)
    plt.plot (x,y)
    plt.xlabel ('X')
    plt.ylabel ('Y')
    plt.title ('Graph')
    plt.show ()




if __name__ == "__main__":
    A = (5, 2)
    B = (1, 7)
    prize = (10, 10)
    graph = make_graph(A, B, prize)
    #plot_graph (graph)