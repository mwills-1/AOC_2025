import numpy as np 

class Vertex:
    def __init__ (self, name, location, weight = 1):
        self.neighbors = []
        self.name = name
        self.weight = weight
        self.id = np.random.rand()
        self.location = location

    def add_neighbor (self, v):
        self.neighbors.append(v)
    
    def norm (self):
        return np.linalg.norm (self.location)
    
    def is_connected (self, v):
        for ver in self.neighbors:
            if ver == v:
                return True
        return False
    
    def __eq__ (self, other):
        return self.name == other.name and self.id == other.id 
    

class Graph:
    """
    A undireted weighted graph
    """
    def __init__ (self):
        self.vertices = []
    
    def add_vertex (self, v):
        self.vertices.append(v)

    def add_node (self, name, location):
        self.add_vertex (Vertex (name, location))
    
    def in_graph (self, v):
        """
        Checks if v is in the graph
        """

        for ver in self.vertices:
            if ver == v:
                return True
        return False
    
    def add_edge (self, v1, v2):
        """
        Adds an edge between the two vertices. Adds v1 and v2 if they are not 
        in the graph already. 
        """
        if not self.in_graph(v1):
            self.add_vertex (v1)
        if not self.in_graph(v2):
            self.add_vertex (v2)
        
        if not v1.is_connected (v2):
            v1.neighbors.append (v2)

        if not v2.is_connected (v1):
            v2.neighbors.append (v1)

        # remove duplicates just in case

        



            

                
                

        



    
