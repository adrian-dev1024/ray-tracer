import abc

from src.matrix import Point, Matrix
from src.ray import Ray
from src.scene import Material


class Shape(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def material(self) -> Material:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def transform(self) -> Matrix:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def center(self) -> Point:
        raise NotImplementedError

    @abc.abstractmethod
    def intersect(self, ray: Ray):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def normal_at(self, point: Point):
        """Extract text from the data set"""
        raise NotImplementedError
