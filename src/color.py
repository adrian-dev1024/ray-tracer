from dataclasses import dataclass
from decimal import Decimal


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

    def __str__(self):
        return f'(r={self.red},g={self.green},b={self.blue})'
