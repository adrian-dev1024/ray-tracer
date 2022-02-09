import math
from dataclasses import dataclass
from decimal import Decimal
from functools import cached_property

from src.canvas import Canvas
from src.matrix import Matrix, IdentityMatrix, Point
from src.ray import Ray
from src.world import World


@dataclass(frozen=True)
class Camera:
    h_size: int
    v_size: int
    field_of_view: Decimal
    transform: Matrix = IdentityMatrix()

    @cached_property
    def half_view(self):
        return Decimal(math.tan(self.field_of_view / 2))

    @cached_property
    def aspect(self):
        return Decimal(self.h_size / self.v_size)

    @cached_property
    def half_width(self):
        if self.aspect >= 1:
            return Decimal(self.half_view)
        return Decimal(self.half_view * self.aspect)

    @cached_property
    def half_height(self):
        if self.aspect >= 1:
            return Decimal(self.half_view / self.aspect)
        return Decimal(self.half_view)

    @cached_property
    def pixel_size(self):
        return Decimal((self.half_width * 2) / self.h_size)

    def ray_for_pixel(self, x, y):
        x_offset = Decimal(x + 0.5) * self.pixel_size
        y_offset = Decimal(y + 0.5) * self.pixel_size

        world_x = self.half_width - x_offset
        world_y = self.half_height - y_offset

        pixel = self.transform.inverse() * Point(world_x, world_y, -1)
        origin = self.transform.inverse() * Point(0, 0, 0)
        direction = (pixel - origin).normalize()

        return Ray(origin, direction)

    def render(self, world: World):
        canvas = Canvas(self.h_size, self.v_size)

        for y in range(self.v_size - 1):
            for x in range(self.h_size - 1):
                ray = self.ray_for_pixel(x, y)
                color = world.color_at(ray)
                canvas.write_pixel(x, y, color)

        return canvas
