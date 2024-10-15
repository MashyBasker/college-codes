import matplotlib.pyplot as plt
from sortedcontainers import SortedDict

class VertexType:
    START, END, SPLIT, MERGE, REGULAR = range(5)

class Vertex:
    def _init_(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.type = None
        self.helper = None

    def _lt_(self, other):
        if self.y != other.y:
            return self.y > other.y
        return self.x < other.x

def determine_vertex_type(vertex, prev_vertex, next_vertex):
    if prev_vertex.y < vertex.y and next_vertex.y < vertex.y:
        if is_ccw(prev_vertex, vertex, next_vertex):
            return VertexType.START
        else:
            return VertexType.SPLIT
    elif prev_vertex.y > vertex.y and next_vertex.y > vertex.y:
        if is_ccw(prev_vertex, vertex, next_vertex):
            return VertexType.END
        else:
            return VertexType.MERGE
    else:
        return VertexType.REGULAR

def is_ccw(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) > 0

def partition_polygon(vertices):
    n = len(vertices)
    vertex_objects = [Vertex(vertices[i][0], vertices[i][1], i) for i in range(n)]
    for i in range(n):
        prev_vertex = vertex_objects[(i - 1) % n]
        next_vertex = vertex_objects[(i + 1) % n]
        vertex_objects[i].type = determine_vertex_type(vertex_objects[i], prev_vertex, next_vertex)

    vertex_objects.sort(key=lambda v: (-v.y, v.x))

    edge_tree = SortedDict()
    diagonals = []

    def add_diagonal(u, v):
        diagonals.append((u.index, v.index))

    for vertex in vertex_objects:
        if vertex.type == VertexType.START:
            edge_tree[vertex] = vertex
        elif vertex.type == VertexType.END:
            if vertex in edge_tree:
                helper = edge_tree.pop(vertex)
                if helper.type == VertexType.MERGE:
                    add_diagonal(helper, vertex)
        elif vertex.type == VertexType.SPLIT:
            edge_index = edge_tree.bisect_left(vertex) - 1
            if edge_index >= 0:
                edge_key = list(edge_tree.keys())[edge_index]
                helper = edge_tree[edge_key]
                add_diagonal(helper, vertex)
                edge_tree[vertex] = vertex
        elif vertex.type == VertexType.MERGE:
            if vertex in edge_tree:
                helper = edge_tree.pop(vertex)
                if helper.type == VertexType.MERGE:
                    add_diagonal(helper, vertex)
            edge_index = edge_tree.bisect_left(vertex) - 1
            if edge_index >= 0:
                edge_key = list(edge_tree.keys())[edge_index]
                helper = edge_tree[edge_key]
                if helper.type == VertexType.MERGE:
                    add_diagonal(helper, vertex)
                edge_tree[vertex] = vertex
        elif vertex.type == VertexType.REGULAR:
            if vertex.y < vertex_objects[(vertex.index - 1) % n].y:
                if vertex in edge_tree:
                    helper = edge_tree.pop(vertex)
                    if helper.type == VertexType.MERGE:
                        add_diagonal(helper, vertex)
                edge_tree[vertex] = vertex
            else:
                edge_index = edge_tree.bisect_left(vertex) - 1
                if edge_index >= 0:
                    edge_key = list(edge_tree.keys())[edge_index]
                    helper = edge_tree[edge_key]
                    if helper.type == VertexType.MERGE:
                        add_diagonal(helper, vertex)
                    edge_tree[vertex] = vertex

    return diagonals

def plot_polygon_with_diagonals(vertices, diagonals):
    plt.figure()
    x, y = zip(*vertices)
    plt.fill(x, y, edgecolor='black', fill=False)  # Draw the polygon

    for diagonal in diagonals:
        start, end = diagonal
        x_coords = [vertices[start][0], vertices[end][0]]
        y_coords = [vertices[start][1], vertices[end][1]]
        plt.plot(x_coords, y_coords, 'r--')  # Draw the diagonal

    plt.scatter(x, y, color='blue')  # Plot the vertices
    for i, (vx, vy) in enumerate(vertices):
        plt.text(vx, vy, f'{i}', fontsize=12, ha='right')  # Label vertices

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage
vertices = [(1, 1),(2,2), (3, 1),(4, 3), (5, 1),(5, 6) , (4, 4) ,(3,7),(2,5),(1, 8)]
diagonals = partition_polygon(vertices)
print("Diagonals to make the polygon monotone:", diagonals)
plot_polygon_with_diagonals(vertices, diagonals)