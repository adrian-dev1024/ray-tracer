import math
from decimal import Decimal

from src.canvas import Canvas
from src.color import Color
from src.matrix import Point, ScalingMatrix, RotationMatrix, ShearingMatrix
from src.ray import Ray
from src.scene import Material, LightPoint
from src.sphere import Sphere

if __name__ == '__main__':
    color = Color(1, 0, 0)
    canvas_pixels = 100
    canvas = Canvas(canvas_pixels, canvas_pixels)

    ray_origin = Point(0, 0, -5)
    wall_z = 10
    wall_size = 7.0
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    # shape = Sphere()
    # shape = Sphere(transform=ScalingMatrix(1, 0.5, 1))
    # shape = Sphere(transform=ScalingMatrix(0.5, 1, 1))
    # shape = Sphere(transform=(RotationMatrix(z_radians=Decimal(math.pi)/4) * ScalingMatrix(0.5, 1, 1)))
    # shape = Sphere(transform=(ScalingMatrix(0.5, 1, 1).rotate(z_radians=Decimal(math.pi)/4)))
    # shape = Sphere(transform=(ShearingMatrix(1, 0, 0, 0, 0, 0) * ScalingMatrix(0.5, 1, 1)))
    # shape = Sphere(transform=(ScalingMatrix(0.5, 1, 1).shear(1, 0, 0, 0, 0, 0)))

    material = Material(Color(1, 0.2, 1))
    shape = Sphere(material=material)
    # shape = Sphere(material=material, transform=ScalingMatrix(0.75, 1, 1))
    # shape = Sphere(material=material, transform=ScalingMatrix(0.5, 1, 1).shear(1, 0, 0, 0, 0, 0))
    # white light behind, above and to the left of the eye
    light_position = Point(-10, 10, -10)
    light_color = Color(1, 1, 1)
    light = LightPoint(light_position, light_color)

    for y in range(canvas_pixels):
        world_y = half - pixel_size * y
        for x in range(canvas_pixels):
            world_x = -half + pixel_size * x
            position = Point(world_x, world_y, wall_z)
            r = Ray(ray_origin, (position - ray_origin).normalize())
            xs = shape.intersect(r)
            if xs.hit():
                hit = xs.hit()
                point = r.position(hit.t)
                normal = hit.obj.normal_at(point)
                eye = -r.direction
                color = hit.obj.material.lighting(light, point, eye, normal)
                canvas.write_pixel(x, y, color)

    with open('/tmp/sphere_3D.ppm', mode='w') as f:
        f.write(canvas.to_ppm())
