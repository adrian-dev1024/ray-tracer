import abc

from src.matrix import Point
from src.ray import Ray


class Shape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def intersect(self, ray: Ray):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def normal_at(self, point: Point):
        """Extract text from the data set"""
        raise NotImplementedError
