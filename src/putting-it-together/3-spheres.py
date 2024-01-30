import math
import os
from decimal import Decimal

from src.camera import Camera
from src.color import Color
from src.matrix import ScalingMatrix, TranslationMatrix, RotationMatrix, Point, Vector, ShearingMatrix
from src.scene import Material, LightSource, PointOfView
from src.shapes.sphere import Sphere
from src.world import World

if __name__ == '__main__':
    floor_transform = ScalingMatrix(10, 0.01, 10)
    floor_material = Material(color=Color(1, 0.9, 0.9), specular=Decimal('0.3'))

    floor = Sphere(
        transform=floor_transform,
        material=floor_material,
        name='floor'
    )

    left_wall_transform = TranslationMatrix(0, 0, 5) * RotationMatrix(y_radians=-math.pi / 4) * RotationMatrix(
        x_radians=math.pi / 2) * ScalingMatrix(10, 0.01, 10)

    left_wall = Sphere(
        transform=left_wall_transform,
        material=floor_material,
        name='left_wall'
    )

    right_wall_transform = TranslationMatrix(0, 0, 5) * RotationMatrix(y_radians=math.pi / 4) * RotationMatrix(
        x_radians=math.pi / 2) * ScalingMatrix(10, 0.01, 10)

    right_wall = Sphere(
        transform=right_wall_transform,
        material=floor_material,
        name='right_wall'
    )

    middle_transform = TranslationMatrix(-0.5, 1, 0.5) * ScalingMatrix(1, 0.33, 1)
    middle_material = Material(color=Color(0.1, 1, 0.5),
                               diffuse=Decimal(0.7),
                               specular=Decimal(0.3))

    middle = Sphere(
        transform=middle_transform,
        material=middle_material,
        name='middle'
    )

    right_transform = TranslationMatrix(1.5, 0.5, -0.5) * ScalingMatrix(0.5, 0.5, 0.5) * ShearingMatrix(x_y=0.33)
    right_material = Material(color=Color(0.75, 1, 0.1),
                              diffuse=Decimal(0.7),
                              specular=Decimal(0.3))
    right = Sphere(
        transform=right_transform,
        material=right_material,
        name='right'
    )

    left_transform = TranslationMatrix(-1.5, 0.33, -0.75) * ScalingMatrix(0.33, 1, 0.33)
    left_material = Material(color=Color(1, 0.8, 0.1),
                             diffuse=Decimal(0.7),
                             specular=Decimal(0.3))

    left = Sphere(
        transform=left_transform,
        material=left_material,
        name='left'
    )
    light_source = LightSource(Point(-10, 10, -10), Color(1, 1, 1))

    world = World(shapes=[floor, right_wall, left_wall, middle, left, right],
                  light_source=light_source)

    pov = PointOfView(Point(0, 1.5, -5),
                      Point(0, 1, 0),
                      Vector(0, 1, 0))
    camera = Camera(400, 200, Decimal(math.pi / 3), transform=pov.transform())

    # canvas = camera.render(world)
    canvas = camera.parallel_render(world)

    with open('/tmp/3_spheres.ppm', mode='w') as f:
        f.write(canvas.to_ppm())

    os.system('open /tmp/3_spheres.ppm')
