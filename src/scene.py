import math
from dataclasses import dataclass
from decimal import Decimal, ROUND_UP

from src.color import Color
from src.matrix import Point


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
