import math
from dataclasses import dataclass


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
        )

    # TODO: Only works for 2 point to get a vector
    def __sub__(self, other):
        return Coordinate(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w
        )

    def __neg__(self):
        return Coordinate(0, 0, 0, 0) - self

    def __mul__(self, other):
        scalar = float(other)
        return Coordinate(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
            self.w * scalar
        )

    def __truediv__(self, other):
        scalar = float(other)
        return Coordinate(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar,
            self.w / scalar
        )

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
            self.x * other.y - self.y * other.x)
