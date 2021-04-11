from dataclasses import dataclass

from src.coordinates import Point, Vector


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


if __name__ == '__main__':
    projectile = Projectile(Point(0, 1, 0), (Vector(1, 1, 0)).normalize() * 2)
    environment = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))

    print(projectile)
    while projectile.position.y > 0.0:
        projectile = projectile.tick(environment)
        print(projectile)
