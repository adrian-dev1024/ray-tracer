from dataclasses import dataclass, field

from src.intersection import Intersections, Intersection
from src.matrix import Point, Matrix, Vector, point, identity_matrix
from src.ray import Ray
from src.scene import Material, material
from src.shapes.shape import Shape


@dataclass
class Sphere(Shape):
    name: str = field(default='Sphere')
    center: Point = field(default_factory=point)
    transform: Matrix = field(default_factory=identity_matrix)
    material: Material = field(default_factory=material)

    def intersect(self, ray: Ray):
        transformed_ray = ray.transform(self.transform.inverse())
        sphere_to_ray = transformed_ray.origin - self.center
        a = transformed_ray.direction.dot(transformed_ray.direction)
        b = 2 * transformed_ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant < 0:
            return Intersections()
        t_1 = ((-b) - discriminant.sqrt()) / (2 * a)
        t_2 = ((-b) + discriminant.sqrt()) / (2 * a)

        return Intersections(Intersection(t_1, self), Intersection(t_2, self))

    def normal_at(self, point: Point):
        object_point = self.transform.inverse() * point
        object_normal = object_point - self.center
        world_normal = self.transform.inverse().transpose() * object_normal
        return Vector(world_normal.x, world_normal.y, world_normal.z).normalize()
