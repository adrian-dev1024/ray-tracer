"""
Chapter 1
"""
import logging
from dataclasses import dataclass

from src.canvas import Canvas
from src.color import Color
from src.coordinates import Point, Vector

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@dataclass
class Environment:
    gravity: Vector
    wind: Vector


@dataclass
class Projectile:
    position: Point
    velocity: Vector

    def tick(self, env: Environment):
        return Projectile(
            self.position + self.velocity,
            self.velocity + env.gravity + env.wind
        )


def plot(canvas: Canvas, position: Point):
    color = Color(1, 0, 0)
    try:
        canvas.write_pixel(round(position.x), round(canvas.height - position.y), color)
        logger.info(f'Plotted x: {round(position.x)}, y: {round(position.y)} => {round(position.y - canvas.height)}')
    except IndexError:
        logger.error(f'Could not plot x: {round(position.x)}, y: {round(position.y - canvas.height)}')


def fire_cannon(projectile: Projectile, env: Environment):
    canvas = Canvas(900, 550)
    while projectile.position.y > 0.0:
        plot(canvas, projectile.position)
        projectile = projectile.tick(env)

    return canvas


if __name__ == '__main__':
    start = Point(0, 1, 0)
    velocity = Vector(1, 1.8, 0).normalize() * 11.25
    projectile = Projectile(start, velocity)
    environment = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))
    canvas = fire_cannon(projectile, environment)
    with open('/tmp/cannon.ppm', mode='w') as f:
        f.write(canvas.to_ppm())
