from dataclasses import dataclass

from src.color import Color
from src.matrix import Point


@dataclass
class LightPoint:
    position: Point
    intensity: Color


@dataclass
class Material:
    color: Color = Color(1, 1, 1)
    ambient: float = 0.1
    diffuse: float = 0.9
    specular: float = 0.9
    shininess: float = 200.0
