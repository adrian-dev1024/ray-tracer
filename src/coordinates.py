from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['x', 'y', 'z', 'w'])


def is_a_point(coordinate: Coordinate):
    return coordinate.w == Point.w


def is_a_vector(coordinate: Coordinate):
    return coordinate.w == Vector.w


class Point:
    w = 1.

    def __init__(self, x, y, z):
        self.coordinate = Coordinate(x, y, z, self.w)


class Vector:
    w = 0.

    def __init__(self, x, y, z):
        self.coordinate = Coordinate(x, y, z, self.w)
