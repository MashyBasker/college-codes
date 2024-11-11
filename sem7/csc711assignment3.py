# -*- coding: utf-8 -*-
"""CSC711Assignment3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qCSrhhoy6MqXhCZnh287FFf0LG-MCFcm
"""

import heapq
from sortedcontainers import SortedList
import matplotlib.pyplot as plt

class EventPoint:
    def __init__(self, x, y, seg=None, is_left=False):
        self.x = x
        self.y = y
        self.seg = seg
        self.is_left = is_left

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __repr__(self):
        return f"EventPoint(x={self.x}, y={self.y}, seg={self.seg}, is_left={self.is_left})"

class Segment:
    def __init__(self, p1, p2):
        if p1[0] > p2[0]:
            p1, p2 = p2, p1
        self.p1 = p1
        self.p2 = p2

    def __lt__(self, other):
        if self is None or other is None:
            return False
        return (self.p1[1], self.p2[1]) < (other.p1[1], other.p2[1])

    def __repr__(self):
        return f"Segment(p1={self.p1}, p2={self.p2})"

def compute_intersection(seg1, seg2):
    x1, y1 = seg1.p1
    x2, y2 = seg1.p2
    x3, y3 = seg2.p1
    x4, y4 = seg2.p2

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None

    intersect_x = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    intersect_y = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom

    if (min(x1, x2) <= intersect_x <= max(x1, x2) and
        min(x3, x4) <= intersect_x <= max(x3, x4) and
        min(y1, y2) <= intersect_y <= max(y1, y2) and
        min(y3, y4) <= intersect_y <= max(y3, y4)):
        return (intersect_x, intersect_y)
    return None

def plot_segments(segments, intersections, sweep_line_x=None):
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot segments
    for seg in segments:
        ax.plot([seg.p1[0], seg.p2[0]], [seg.p1[1], seg.p2[1]], 'b-')

    # Plot intersections
    if intersections:
        x, y = zip(*intersections)
        ax.scatter(x, y, c='r', marker='x')

    # Plot sweep line if specified
    if sweep_line_x is not None:
        ax.axvline(x=sweep_line_x, color='g', linestyle='--', label='Sweep Line')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Line Segment Intersections')
    plt.grid(True)
    plt.legend()
    plt.show()

def plane_sweep(segments):
    event_queue = []
    status = SortedList()

    # Populate event queue
    for seg in segments:
        heapq.heappush(event_queue, EventPoint(seg.p1[0], seg.p1[1], seg, is_left=True))
        heapq.heappush(event_queue, EventPoint(seg.p2[0], seg.p2[1], seg, is_left=False))

    intersections = []

    while event_queue:
        event = heapq.heappop(event_queue)
        print(f"Processing event: {event}")

        # Plot the current state of the sweep line
        plot_segments(segments, intersections, sweep_line_x=event.x)

        if event.is_left:
            status.add(event.seg)
            idx = status.index(event.seg) if event.seg in status else None
            if idx is not None:
                seg_above = status[idx + 1] if idx + 1 < len(status) else None
                seg_below = status[idx - 1] if idx - 1 >= 0 else None

                if seg_above:
                    intersect = compute_intersection(event.seg, seg_above)
                    if intersect:
                        print(f"Found intersection between {event.seg} and {seg_above} at {intersect}")
                        heapq.heappush(event_queue, EventPoint(intersect[0], intersect[1], seg=None))
                        intersections.append(intersect)

                if seg_below:
                    intersect = compute_intersection(event.seg, seg_below)
                    if intersect:
                        print(f"Found intersection between {event.seg} and {seg_below} at {intersect}")
                        heapq.heappush(event_queue, EventPoint(intersect[0], intersect[1], seg=None))
                        intersections.append(intersect)

        else:
            if event.seg in status:
                idx = status.index(event.seg) if event.seg in status else None
                if idx is not None:
                    seg_above = status[idx + 1] if idx + 1 < len(status) else None
                    seg_below = status[idx - 1] if idx - 1 >= 0 else None

                    if seg_above and seg_below:
                        intersect = compute_intersection(seg_above, seg_below)
                        if intersect:
                            print(f"Found intersection between {seg_above} and {seg_below} at {intersect}")
                            heapq.heappush(event_queue, EventPoint(intersect[0], intersect[1], seg=None))
                            intersections.append(intersect)

                    status.remove(event.seg)

    return intersections

# Example Usage
segments = [
    Segment((1, 3), (4, 1)),
    Segment((1, 2), (4, 3)),
    Segment((2, 4), (5, 2)),
    Segment((3, 1), (6, 4))
]


intersections = plane_sweep(segments)
print("Intersections:", intersections)

# Plot the segments and intersections without the sweep line
plot_segments(segments, intersections)