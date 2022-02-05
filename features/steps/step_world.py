"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from decimal import Decimal

from behave import given, then, when

from src.color import Color
from src.matrix import Point, ScalingMatrix, Vector
from src.ray import Ray
from src.scene import World, LightPoint, Material, default_world, Sphere


@given('w ← World()')
def step_impl(context):
    context.w = World()


@given('light_source ← LightPoint(Point(-10, 10, -10), Color(1, 1, 1))')
def step_impl(context):
    context.light_source = LightPoint(Point(-10, 10, -10), Color(1, 1, 1))


@given('s1 ← Sphere(material=Material(color=Color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)')
def step_impl(context):
    context.s1 = Sphere(material=Material(color=Color(0.8, 1.0, 0.6), diffuse=Decimal(0.7), specular=Decimal(0.2)))


@given('s2 ← Sphere(transform=ScalingMatrix(0.5, 0.5, 0.5))')
def step_impl(context):
    context.s2 = Sphere(transform=ScalingMatrix(0.5, 0.5, 0.5))


@given('w ← default_world()')
def step_impl(context):
    context.w = default_world()


# @given('r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))')
# def step_impl(context):
#     context.r = Ray(Point(0, 0, -5), Vector(0, 0, 1))


@when('w ← default_world()')
def step_impl(context):
    context.w = default_world()


@when('xs ← w.intersect(r)')
def step_impl(context):
    context.xs = context.w.intersect(context.r)


@then('w contains no objects')
def step_impl(context):
    assert len(context.w.objects) == 0


@then('w has no light source')
def step_impl(context):
    assert context.w.light_source is None


@then('w.light_source = light_source')
def step_impl(context):
    assert context.w.light_source == context.light_source


@then('w contains s1')
def step_impl(context):
    assert context.s1 in context.w.objects


@then('w contains s2')
def step_impl(context):
    assert context.s2 in context.w.objects


@then('len(xs) = 4')
def step_impl(context):
    assert len(context.xs) == 4


@then('xs[0].t = 4')
def step_impl(context):
    assert context.xs[1].t == 4.5


@then('xs[1].t = 4.5')
def step_impl(context):
    assert context.xs[2].t == 5.5


@then('xs[2].t = 5.5')
def step_impl(context):
    assert context.xs[3].t == 6


@then('xs[3].t = 6')
def step_impl(context):
    assert context.xs[3].t == 6