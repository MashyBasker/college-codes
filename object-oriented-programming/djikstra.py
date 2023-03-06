import sys

class Djikstra:
    adj_matrix = []
    def __init__(self, n):
        self.vertices = n
        print("Provide the adjacency matrix: ")
        for i in range(n):
            k = [int(x) for x in input().split(" ")]
            Djikstra.adj_matrix.append(k)
            k = []
    
    def display_matrix(self):
        print(Djikstra.adj_matrix)

    def index_with_min_dist(self, distance, visited) -> int:
        #
        # @params: list of distances[distance], list of whether vertex is visited or not[visited] 
        # @return: index of the node with least distance
        #
        inf = sys.maxsize
        min_idx = 0
        for v in range(self.vertices):
            if distance[v] < inf and visited[v] == False:
                inf = distance[v]
                min_idx = v
        return min_idx
    
    def display_solution(self, src, distances):
        # @params: source vertex[src], list of distances[distance]
        print("Source -> Destination\tShortest Distance")
        for v in range(self.vertices):
            if v != src:
                print(f"{src} -> {v}\t\t\t{distances[v]}")
    
    def djikstra(self, src):
        #
        # @params: the source node[src]
        # @return: 2D array containing the shortest distance of each vertex from the source
        #
        distances = [sys.maxsize] * self.vertices
        visited = [False] * self.vertices
        distances[src] = 0

        for v in range(self.vertices):
            mindex = self.index_with_min_dist(distances, visited)
            visited[mindex] = True

            for x in range(self.vertices):
                if Djikstra.adj_matrix[mindex][x] > 0 and visited[x] == False and distances[x] > distances[mindex] +  Djikstra.adj_matrix[mindex][x]:
                    distances[x] = distances[mindex] + Djikstra.adj_matrix[mindex][x]

            
        self.display_solution(src, distances)



def main():
    n = int(input("How many vertices?: "))
    djk = Djikstra(n)
    djk.display_matrix()
    src = int(input("Choose the source: "))
    djk.djikstra(src)

if __name__ == "__main__":
    main()