from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

from src.color import Color
from src.intersection import Intersections, Intersection
from src.matrix import Point, ScalingMatrix, Matrix, IdentityMatrix, Vector
from src.ray import Ray


@dataclass
class LightPoint:
    position: Point
    intensity: Color


@dataclass
class Material:
    color: Color = Color(1, 1, 1)
    ambient: Decimal = Decimal(0.1)
    diffuse: Decimal = Decimal(0.9)
    specular: Decimal = Decimal(0.9)
    shininess: Decimal = Decimal(200.0)

    def lighting(self, light, point, eye_v, normal_v, round_specular=True):
        # combine the surface color with the light's color/intensity
        effective_color = self.color * light.intensity

        # find the direction to the light source
        light_v = (light.position - point).normalize()

        # compute the ambient contribution
        ambient = effective_color * self.ambient

        # light_dot_normal represents the cosine of the angle between the
        # light vector and the normal vector. A negative number means the
        # light is on the other side of the surface.
        light_dot_normal = light_v.dot(normal_v)

        diffuse = Color(0, 0, 0)
        specular = Color(0, 0, 0)
        if light_dot_normal >= 0:
            # compute the diffuse contribution
            diffuse = effective_color * self.diffuse * light_dot_normal

            # reflect_dot_eye represents the cosine of the angle between the
            # reflection vector and the eye vector. A negative number means the
            # light reflects away from the eye.
            reflect_v = (-light_v).reflect(normal_v)
            reflect_dot_eye = reflect_v.dot(eye_v)

            if reflect_dot_eye > 0:
                # compute the specular contribution
                factor = reflect_dot_eye ** self.shininess
                specular = light.intensity * self.specular * factor

            if round_specular:
                # rounding to the tenth
                specular.red = specular.red.quantize(Decimal('0.1'))
                specular.blue = specular.blue.quantize(Decimal('0.1'))
                specular.green = specular.green.quantize(Decimal('0.1'))

        return ambient + diffuse + specular


@dataclass
class World:
    objects: List = field(default_factory=lambda: [])
    light_source: LightPoint = None

    def intersect(self, ray: Ray):
        intersections = Intersections()
        for o in self.objects:
            intersections += o.intersect(ray)
        intersections.sort(key=lambda i: i.t)
        return intersections


def default_world():
    return World(
        objects=[
            Sphere(material=Material(color=Color(0.8, 1.0, 0.6), diffuse=Decimal(0.7), specular=Decimal(0.2))),
            Sphere(transform=ScalingMatrix(0.5, 0.5, 0.5))
        ],
        light_source=LightPoint(Point(-10, 10, -10), Color(1, 1, 1))
    )


@dataclass
class Sphere:
    center: Point = Point(0, 0, 0)
    transform: Matrix = IdentityMatrix(4)
    material: Material = Material()

    def intersect(self, ray: Ray):
        ray = ray.transform(self.transform.inverse())
        sphere_to_ray = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return Intersections()
        t_1 = (-b - discriminant.sqrt()) / (2 * a)
        t_2 = (-b + discriminant.sqrt()) / (2 * a)

        return Intersections(Intersection(t_1, self), Intersection(t_2, self))

    def normal_at(self, point: Point):
        object_point = self.transform.inverse() * point
        object_normal = object_point - self.center
        world_normal = self.transform.inverse().transpose() * object_normal
        return Vector(world_normal.x, world_normal.y, world_normal.z).normalize()
