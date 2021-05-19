from dataclasses import dataclass

from src.matrix import Point, Vector


@dataclass
class Ray:

    origin: Point
    direction: Vector

    def position(self, t):
        return self.origin + self.direction * t
