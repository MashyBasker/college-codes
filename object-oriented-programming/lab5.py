import sys

class CityDistance:
    distmat = []
    def __init__(self, n):
        self.vertices = n
        print("Provide the distance between cities as matrices: ")
        for _ in range(n):
            k = input().split(" ")
            p = []
            for s in k: 
                if s != "inf":
                    p.append(int(s))
                elif s == "inf":
                    p.append(sys.maxsize)
            CityDistance.distmat.append(p)
            k = []
        

    def floyd_warshall(self):
        dist = [x.copy() for x in CityDistance.distmat]
        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist
    
    def solution(self):
        ans = self.floyd_warshall()
        # print(ans)
        c1 = int(input("Enter the source city number: "))
        c2 = int(input("Enter the destination city number: "))
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i == c1 and j == c2:
                    print(f"City {c1} <------ {ans[i][j]} ------> City {c2}")


def main():
    n = int(input("How many cities?: "))
    dstm = CityDistance(n)
    dstm.solution()

if __name__ == "__main__":
    main()



