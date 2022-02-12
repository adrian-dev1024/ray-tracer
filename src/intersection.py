from collections import UserList
from dataclasses import dataclass
from decimal import Decimal

from src.matrix import Vector, Point
from src.ray import Ray
from src.shapes.shape import Shape


@dataclass
class IntersectionPreComputedValues:
    t: Decimal
    shape: Shape
    point: Point
    eyeVec: Vector
    normalVec: Vector
    inside: bool


@dataclass
class Intersection:
    t: Decimal
    shape: Shape

    def pre_compute(self, ray: Ray):
        point = ray.position(self.t)
        normalVec = self.shape.normal_at(point)
        eyeVec = -ray.direction
        inside = False
        if normalVec.dot(eyeVec) < 0:
            normalVec = -normalVec
            inside = True

        return IntersectionPreComputedValues(
            self.t,
            self.shape,
            point,
            eyeVec,
            normalVec,
            inside
        )


class Intersections(UserList):

    def __init__(self, *args):
        # TODO: Probably Should verify that all args are of type Intersection
        super(Intersections, self).__init__(args)
        self.sort(key=lambda item: item.t)

    def hit(self):
        hit = None
        for i in self.data:
            if i.t >= 0:
                hit = i
                break
        return hit
