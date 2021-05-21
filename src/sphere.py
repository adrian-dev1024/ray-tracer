from dataclasses import dataclass

from src.intersection import Intersection, Intersections
from src.matrix import Point, Matrix, IdentityMatrix
from src.ray import Ray


@dataclass
class Sphere:
    center: Point = Point(0, 0, 0)
    transform: Matrix = IdentityMatrix(4)

    def intersect(self, ray: Ray):
        ray = ray.transform(self.transform.inverse())
        sphere_to_ray = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return []
        t_1 = (-b - discriminant.sqrt()) / (2 * a)
        t_2 = (-b + discriminant.sqrt()) / (2 * a)

        return Intersections(Intersection(t_1, self), Intersection(t_2, self))
