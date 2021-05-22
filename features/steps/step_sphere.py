"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
import math
from decimal import Decimal

from behave import given, then, when

from src.matrix import Point, Vector, TranslationMatrix, IdentityMatrix, ScalingMatrix, RotationMatrix
from src.scene import Material
from src.ray import Ray
from src.sphere import Sphere


@given('r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))')
def step_impl(context):
    context.r = Ray(Point(0, 0, -5), Vector(0, 0, 1))


@given('r ← Ray(Point(0, 1, -5), Vector(0, 0, 1))')
def step_impl(context):
    context.r = Ray(Point(0, 1, -5), Vector(0, 0, 1))


@given('r ← Ray(Point(0, 2, -5), Vector(0, 0, 1))')
def step_impl(context):
    context.r = Ray(Point(0, 2, -5), Vector(0, 0, 1))


@given('r ← Ray(Point(0, 0, 0), Vector(0, 0, 1))')
def step_impl(context):
    context.r = Ray(Point(0, 0, 0), Vector(0, 0, 1))


@given('r ← Ray(Point(0, 0, 5), Vector(0, 0, 1))')
def step_impl(context):
    context.r = Ray(Point(0, 0, 5), Vector(0, 0, 1))


@given('s ← Sphere()')
def step_impl(context):
    context.s = Sphere()


@given('s ← Sphere(transform=ScalingMatrix(2, 2, 2))')
def step_impl(context):
    context.s = Sphere(transform=ScalingMatrix(2, 2, 2))


@given('s ← Sphere(transform=TranslationMatrix(5, 0, 0))')
def step_impl(context):
    context.s = Sphere(transform=TranslationMatrix(5, 0, 0))


@given('t ← TranslationMatrix(2, 3, 4)')
def step_impl(context):
    context.t = TranslationMatrix(2, 3, 4)


@given('s ← Sphere(transform=TranslationMatrix(0, 1, 0))')
def step_impl(context):
    context.s = Sphere(transform=TranslationMatrix(0, 1, 0))


@given('s ← sphere(transform=RotationMatrix(z_radians=π/5).scale(1, 0.5, 1))')
def step_impl(context):
    context.s = Sphere(transform=RotationMatrix(z_radians=Decimal(math.pi) / 5).scale(1, 0.5, 1))


@given('m.ambient ← 1')
def step_impl(context):
    context.m.ambient = 1


@when('xs ← s.intersect(r)')
def step_impl(context):
    context.xs = context.s.intersect(context.r)


@when('s.transform ← t')
def step_impl(context):
    context.s.transform = context.t


@when('n ← s.normal_at(Point(1, 0, 0))')
def step_impl(context):
    context.n = context.s.normal_at(Point(1, 0, 0))


@when('n ← s.normal_at(Point(0, 1, 0))')
def step_impl(context):
    context.n = context.s.normal_at(Point(0, 1, 0))


@when('n ← s.normal_at(Point(0, 0, 1))')
def step_impl(context):
    context.n = context.s.normal_at(Point(0, 0, 1))


@when('n ← s.normal_at(Point(√3/3, √3/3, √3/3))')
def step_impl(context):
    context.n = context.s.normal_at(Point(Decimal(3).sqrt() / 3, Decimal(3).sqrt() / 3, Decimal(3).sqrt() / 3))


@when('n ← s.normal_at(Point(0, 1.70711, -0.70711))')
def step_impl(context):
    context.n = context.s.normal_at(Point(0, 1.70711, -0.70711))


@when('n ← s.normal_at(Point(0, √2/2, -√2/2))')
def step_impl(context):
    context.n = context.s.normal_at(Point(0, Decimal(2).sqrt() / 2, Decimal(2).sqrt() / 2))

@when('s.material ← m')
def step_impl(context):
    context.s.material = context.m


@then('len(xs) = 2')
def step_impl(context):
    assert len(context.xs) == 2


@then('len(xs) = 0')
def step_impl(context):
    assert len(context.xs) == 0


@then('xs[0].t = 4.0')
def step_impl(context):
    assert context.xs[0].t == 4.0


@then('xs[1].t = 6.0')
def step_impl(context):
    assert context.xs[1].t == 6.0


@then('xs[0].t = 5.0')
def step_impl(context):
    assert context.xs[0].t == 5.0


@then('xs[1].t = 5.0')
def step_impl(context):
    assert context.xs[1].t == 5.0


@then('xs[0].t = -1.0')
def step_impl(context):
    assert context.xs[0].t == -1.0


@then('xs[1].t = 1.0')
def step_impl(context):
    assert context.xs[1].t == 1.0


@then('xs[0].t = -6.0')
def step_impl(context):
    assert context.xs[0].t == -6.0


@then('xs[1].t = -4.0')
def step_impl(context):
    assert context.xs[1].t == -4.0


@then('xs[0].obj = s')
def step_impl(context):
    assert context.xs[0].obj == context.s


@then('xs[1].obj = s')
def step_impl(context):
    assert context.xs[1].obj == context.s


@then('s.transform = IdentityMatrix(4)')
def step_impl(context):
    assert context.s.transform == IdentityMatrix(4)


@then('s.transform = t')
def step_impl(context):
    assert context.s.transform == context.t


@then('xs[0].t = 3')
def step_impl(context):
    assert context.xs[0].t == 3


@then('xs[1].t = 7')
def step_impl(context):
    assert context.xs[1].t == 7


@then('n = Vector(1, 0, 0)')
def step_impl(context):
    assert context.n == Vector(1, 0, 0)


@then('n = Vector(0, 1, 0)')
def step_impl(context):
    assert context.n == Vector(0, 1, 0)


@then('n = Vector(0, 0, 1)')
def step_impl(context):
    assert context.n == Vector(0, 0, 1)


@then('n = Vector(√3/3, √3/3, √3/3)')
def step_impl(context):
    assert context.n == Vector(Decimal(3).sqrt() / 3, Decimal(3).sqrt() / 3, Decimal(3).sqrt() / 3)


@then('n = n.normalize()')
def step_impl(context):
    assert context.n == context.n.normalize()


@then('n = Vector(0, 0.70711, -0.70711)')
def step_impl(context):
    assert context.n == Vector(0, 0.70711, -0.70711)


@then('n = Vector(0, 0.97014, -0.24254)')
def step_impl(context):
    assert context.n == Vector(0, 0.97014, -0.24254)


@then('s.material = Material()')
def step_impl(context):
    assert context.s.material == Material()


@then('s.material = m')
def step_impl(context):
    assert context.s.material == context.m
