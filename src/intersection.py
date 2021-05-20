from collections import UserList
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Intersection:
    t: Decimal
    obj: object


class Intersections(UserList):
    
    def __init__(self, *args):
        super(Intersections, self).__init__(args)
