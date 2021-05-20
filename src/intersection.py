from collections import UserList
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Intersection:
    t: Decimal
    obj: object


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

