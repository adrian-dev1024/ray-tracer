"""
Chapter 4
"""
import math
from decimal import Decimal

from src.canvas import Canvas
from src.color import Color
from src.matrix import Point


def draw(canvas, point):
    scale = canvas.width * 3 / 8
    scaled_point = point.scale(scale, scale, 0).translate(round(canvas.width/2), round(canvas.height/2), 0)
    canvas.write_pixel(round(scaled_point.x), round(scaled_point.y), color)


if __name__ == '__main__':
    color = Color(1, 0, 0)
    canvas = Canvas(500, 500)
    center = Point(0, 0, 0)
    twelve = Point(0, 1, 0)
    radian = Decimal(3) * Decimal(math.pi) / Decimal(6)
    for hour in range(1, 13):
        current = twelve.rotate(z_radians=Decimal(hour) * Decimal(math.pi) / Decimal(6))
        draw(canvas, current)

    with open('/tmp/clock_face.ppm', mode='w') as f:
        f.write(canvas.to_ppm())
