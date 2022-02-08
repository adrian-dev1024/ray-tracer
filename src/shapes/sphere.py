from dataclasses import dataclass

from src.intersection import Intersections, Intersection
from src.matrix import Point, Matrix, IdentityMatrix, Vector
from src.ray import Ray
from src.scene import Material
from src.shapes.shape import Shape


@dataclass
class Sphere(Shape):
    center: Point = Point(0, 0, 0)
    transform: Matrix = IdentityMatrix(4)
    material: Material = Material()

    def intersect(self, ray: Ray):
        ray = ray.transform(self.transform.inverse())
        sphere_to_ray = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return Intersections()
        t_1 = (-b - discriminant.sqrt()) / (2 * a)
        t_2 = (-b + discriminant.sqrt()) / (2 * a)

        return Intersections(Intersection(t_1, self), Intersection(t_2, self))

    def normal_at(self, point: Point):
        object_point = self.transform.inverse() * point
        object_normal = object_point - self.center
        world_normal = self.transform.inverse().transpose() * object_normal
        return Vector(world_normal.x, world_normal.y, world_normal.z).normalize()
