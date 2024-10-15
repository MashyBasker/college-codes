#!/usr/bin/python

from typing import Tuple, List
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

# Generate "count" number of random points within the range 0..100
# and store them in a list of tuples
def gen_points(count: int) -> List[Tuple[int, int]]:
    X = np.random.randint(0,1001,count)
    Y = np.random.randint(0,1001,count)

    ps = [(x,y) for x,y in zip(X,Y)]
    return ps


# we have 3 points A, B, C on a plane with coords (xa,ya,0), (xb,yb,0) & (xc,yc,0)
# The slope of the line AB = (yb-ya)/(xb-xa)
# The slope of the line BC = (yc-yb)/(xc-xb)
# As they are ordered points, the slopes have the relation
# (yb-ya)/(xb-xa) = K * (yc-yb)/(xc-xb), this value k determines the orientation
# (yb-ya)*(xc-xb) - (xb-xa)*(yc-yb) = k
# if k = 0, the lines AB and AC are in the orientation __, i.e collinear
# if k > 0, the lines AB and AC are in the orientation _/, i.e anti-clockwise
# if k < 0, the lines AB and AC are in the orientation _ , i.e clockwise
#                                                       \
def orientation(
        p: Tuple[int,int], q: Tuple[int,int], r: Tuple[int,int]
) -> int:
    return (q[1] - p[1]) * (r[0] - q[0]) - \
               (q[0] - p[0]) * (r[1] - q[1])

# compute the distance between 2 point tuples using the squared-distance formula
def distance(p1: Tuple[int,int], p2: Tuple[int,int]) -> int | float:
    return sqrt((p1[1] - p2[1])**2 + (p1[0] - p2[0])**2)

# calculate a list of convex hull points using the Jarvis-Marching algorithm
def jarvis(S: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    # S is the point set
    # P is the convext hull points set
    p_leftmost: Tuple[int,int] = min(S, key=lambda p: p[0]) # leftmost point
    idx: int = S.index(p_leftmost)

    P: List[Tuple[int,int]] = [] # list of convex hull points
    n: int = len(S) # calculate |S|

    l: int = idx

    while True:
        P.append(S[l])
        q: int = (l + 1) % n # get the next point in the list
        for i in range(n):
            if i == l:
                continue
            d = orientation(S[l], S[i], S[q])
            if d < 0 or (d == 0 and distance(S[i], S[l]) > distance(S[q], S[l])):
                q = i
        l = q
        if l == idx:
            break
        print(P)
    return P


def main() -> None:
    pointsets: List[Tuple[int,int]] = gen_points(40)
    p_ch = jarvis(pointsets)
    plt.subplot(1,2,1)
    plt.scatter(*zip(*pointsets), label="Points")
    plt.title("Point sets")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend()

    plt.subplot(1,2,2)
    plt.scatter(*zip(*pointsets), label="Points")
    if len(p_ch) > 0:
        ch_x, ch_y = zip(*p_ch)
        plt.plot(ch_x + (ch_x[0],), ch_y + (ch_y[0],), 'r-', label="Convex Hull")
    plt.title("Points with Convex Hull")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
