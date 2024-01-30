from dataclasses import dataclass
from decimal import Decimal

from src import EPSILON


@dataclass
class Color:
    red: Decimal
    green: Decimal
    blue: Decimal

    def __init__(self, red, green, blue):
        self.red = Decimal(red).normalize()
        self.green = Decimal(green).normalize()
        self.blue = Decimal(blue).normalize()

    def __add__(self, other):
        return Color(
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue
        )

    def __sub__(self, other):
        return Color(
            self.red - other.red,
            self.green - other.green,
            self.blue - other.blue
        )

    def __mul__(self, other):
        if isinstance(other, (Decimal, int, float, str)):
            scalar = Decimal(other)
            return Color(
                self.red * scalar,
                self.green * scalar,
                self.blue * scalar
            )
        elif isinstance(other, Color):
            return Color(
                self.red * other.red,
                self.green * other.green,
                self.blue * other.blue
            )
        else:
            return NotImplemented

    def __eq__(self, other):
        return abs(self.red - other.red) < EPSILON and abs(self.green - other.green) < EPSILON and abs(
            self.blue - other.blue) < EPSILON

    def __str__(self):
        return f'(r={self.red},g={self.green},b={self.blue})'


def color():
    return Color(1, 1, 1)
