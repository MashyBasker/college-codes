a = [[2, 3, 5], [5, 6, 7], [1, 2, 3]]
dist = list(map(lambda i: list(map(lambda j: j, i)), a))
j = [x.copy() for x in a]
# print(dist)
# print(j)

a[0][0] = 1
print(a, j, dist, sep="\n")
