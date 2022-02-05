from collections import UserList
from dataclasses import dataclass
from decimal import Decimal

from src.matrix import Vector, Point
from src.ray import Ray


@dataclass
class Intersection:
    t: Decimal
    obj: object

    def pre_compute(self, ray: Ray):
        point = ray.position(self.t)
        return IntersectionPreComputedValues(
            self.t,
            self.obj,
            point,
            ray.direction,
            self.obj.normal_at(point)
        )


class Intersections(UserList):
    
    def __init__(self, *args):
        # TODO: Probably Should to verify that all args are of type Intersection
        super(Intersections, self).__init__(args)
        self.sort(key=lambda item: item.t)

    def hit(self):
        hit = None
        for i in self.data:
            if i.t > 0:
                hit = i
                break
        return hit



@dataclass
class IntersectionPreComputedValues:
    t: Decimal
    obj: object
    point: Point
    eyeVec: Vector
    normalVec: Vector
