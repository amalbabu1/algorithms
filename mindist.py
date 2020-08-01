# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def points_sort(points, n):
    points.sort(key=lambda points: points.x)

    return minimum_distance_squared(points, n)


def distance_squared(first_point, second_point):
    return ((first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2)


def findmin(points):
    min_distance_squared = float("inf")
    for p, q in combinations(points, 2):
        min_distance_squared = min(
            min_distance_squared, distance_squared(p, q))
    return min_distance_squared


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def stripmin(points, d, n):
    minVal = d
    size = n

    for i in range(size):
        for j in range(1, min(8, size - i)):
            if(distance_squared(points[i], points[i+j]) < minVal):
                minVal = distance_squared(points[i], points[i+j])
            j += 1
    return minVal


def minimum_distance_squared(points, n):
    if n <= 4:
        return findmin(points)

    mid = n//2
    midPoint = points[mid]

    dleft = minimum_distance_squared(points[:mid], mid)
    dright = minimum_distance_squared(points[mid:], n-mid)

    d = min(dleft, dright)

    divide = []
    for i in range(0, len(points)):
        if(abs(points[i].x-midPoint.x) < d):
            divide.append(points[i])
    set(divide)
    divide.sort(key=lambda points: points.y)

    return min(d, stripmin(divide, d, len(divide)))


if __name__ == "__main__":
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    assert 1 <= len(input_points) <= 10 ** 5
    set(input_points)
    n = len(input_points)
    print("{0:.9f}".format(sqrt(points_sort(input_points, n))))
