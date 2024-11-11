from collections import defaultdict
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        # Add an undirected edge with given weight
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))

    def prim_mst(self, start=0):
        # Use Prim's algorithm to create an MST
        mst_edges = []
        visited = [False] * self.V
        min_heap = [(0, start, -1)]  # (weight, vertex, parent)

        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            if parent != -1:
                mst_edges.append((parent, u, weight))
            for next_weight, v in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (next_weight, v, u))

        return mst_edges

    def preorder_traversal(self, mst_adj, start=0):
        # Perform preorder traversal to get the TSP path
        path = []
        visited = [False] * self.V

        def dfs(v):
            visited[v] = True
            path.append(v)
            for u in mst_adj[v]:
                if not visited[u]:
                    dfs(u)

        dfs(start)
        return path

    def approx_tsp(self):
        # Find the MST and create adjacency list for the MST
        mst_edges = self.prim_mst(start=1)  # Start from vertex 1 for this example
        mst_adj = defaultdict(list)
        for u, v, weight in mst_edges:
            mst_adj[u].append(v)
            mst_adj[v].append(u)

        # Get the TSP path by performing a preorder traversal on the MST
        tsp_path = self.preorder_traversal(mst_adj, start=1)  # Start traversal from vertex 1

        # Return to the starting point to complete the cycle
        tsp_path.append(tsp_path[0])

        return tsp_path

# Example usage
g = Graph(5)  # Updated to include 5 vertices to allow index 4
g.add_edge(1, 2, 10)
g.add_edge(1, 4, 20)
g.add_edge(1, 3, 15)
g.add_edge(2, 4, 25)
g.add_edge(2, 3, 35)
g.add_edge(4, 3, 30)

tsp_path = g.approx_tsp()
print("Approximate TSP path:", tsp_path)
