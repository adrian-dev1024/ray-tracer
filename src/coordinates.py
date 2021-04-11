import math
from dataclasses import dataclass


class CoordinateNotPoint(Exception):
    pass


class CoordinateNotVector(Exception):
    pass


@dataclass(eq=False)
class Coordinate:
    x: float
    y: float
    z: float
    w: float

    def is_a_point(self):
        return self.w == Point.w

    def is_a_vector(self):
        return self.w == Vector.w

    def __to_point(self):
        if self.is_a_point():
            return Point(self.x, self.y, self.z)
        raise CoordinateNotPoint()

    def __to_vector(self):
        if self.is_a_point():
            return Vector(self.x, self.y, self.z)
        raise CoordinateNotVector()

    def __convert(self):
        if self.is_a_point():
            return Point(self.x, self.y, self.z)
        elif self.is_a_vector():
            return Vector(self.x, self.y, self.z)
        return self

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Coordinate):
            return self.x == other.x and \
                   self.y == other.y and \
                   self.z == other.z and \
                   self.w == other.w
        return NotImplemented

    # TODO: Not sure what happens when adding a point to a point
    def __add__(self, other):
        return Coordinate(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w
        ).__convert()

    # TODO: Only works for 2 point to get a vector
    def __sub__(self, other):
        return Coordinate(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w
        ).__convert()

    def __neg__(self):
        # n = Coordinate(0, 0, 0, 0) - self
        return (Coordinate(0, 0, 0, 0) - self).__convert()

    def __mul__(self, other):
        scalar = float(other)
        return Coordinate(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
            self.w * scalar
        ).__convert()

    def __truediv__(self, other):
        scalar = float(other)
        return Coordinate(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar,
            self.w / scalar
        ).__convert()

@dataclass
class Point(Coordinate):
    w: float = 1.


@dataclass
class Vector(Coordinate):
    w: float = 0.

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        magnitude = self.magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude
        )

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
