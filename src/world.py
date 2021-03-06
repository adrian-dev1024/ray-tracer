from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

from src.color import Color
from src.intersection import Intersections, IntersectionPreComputedValues
from src.matrix import ScalingMatrix, Point
from src.ray import Ray
from src.scene import LightSource, Material
from src.shapes.shape import Shape
from src.shapes.sphere import Sphere


@dataclass
class World:
    shapes: List = field(default_factory=lambda: [])
    light_source: LightSource = None

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)

    def intersect(self, ray: Ray):
        intersections = Intersections()
        for shape in self.shapes:
            intersections += shape.intersect(ray)
        intersections.sort(key=lambda i: i.t)
        return intersections

    def shade_hit(self, comp: IntersectionPreComputedValues):
        return comp.shape.material.lighting(
            self.light_source,
            comp.point,
            comp.eyeVec,
            comp.normalVec,
            in_shadow=self.is_in_shadow(comp.over_point)
        )

    def color_at(self, ray: Ray):
        intersections = self.intersect(ray)

        if not intersections:
            return Color(0, 0, 0)

        hit = intersections.hit()

        if not hit:
            return Color(0, 0, 0)

        return self.shade_hit(hit.pre_compute(ray))

    def is_in_shadow(self, p: Point):
        diff_vector = self.light_source.position - p

        distance = diff_vector.magnitude()
        direction = diff_vector.normalize()

        intersections = self.intersect(Ray(p, direction))

        hit = intersections.hit()

        return hit is not None and hit.t < distance


def default_world():
    return World(
        shapes=[
            Sphere(material=Material(color=Color(0.8, 1.0, 0.6), diffuse=Decimal(0.7), specular=Decimal(0.2))),
            Sphere(transform=ScalingMatrix(0.5, 0.5, 0.5))
        ],
        light_source=LightSource(Point(-10, 10, -10), Color(1, 1, 1))
    )
