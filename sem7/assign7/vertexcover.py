class Graph:
    def __init__(self, vertices):
        # Initialize the graph with the given number of vertices
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        # Add an undirected edge between u and v
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_vertex_cover(self):
        # Set to store the vertex cover
        cover = set()
        
        # Convert adjacency list to a set of edges
        edges = set((u, v) for u in self.adj_list for v in self.adj_list[u])
        
        # While there are edges in the graph
        while edges:
            # Pick an arbitrary edge (u, v)
            (u, v) = edges.pop()
            
            # Add both endpoints of the edge to the cover
            cover.add(u)
            cover.add(v)
            
            # Remove all edges connected to u and v
            edges = {e for e in edges if u not in e and v not in e}
        
        return cover

# Example usage
g = Graph(5)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)

cover = g.find_vertex_cover()
print("Approximate Vertex Cover:", cover)
