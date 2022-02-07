"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from decimal import Decimal

from behave import given, then, when

from src.color import Color
from src.intersection import Intersection
from src.matrix import Point, ScalingMatrix, Vector
from src.ray import Ray
from src.scene import LightSource, Material
from src.world import World, default_world
from src.shapes.sphere import Sphere


@given('w ← World()')
def step_impl(context):
    context.w = World()


@given('light_source ← LightSource(Point(-10, 10, -10), Color(1, 1, 1))')
def step_impl(context):
    context.light_source = LightSource(Point(-10, 10, -10), Color(1, 1, 1))


@given('s1 ← Sphere(material=Material(color=Color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)')
def step_impl(context):
    context.s1 = Sphere(material=Material(color=Color(0.8, 1.0, 0.6), diffuse=Decimal(0.7), specular=Decimal(0.2)))


@given('s2 ← Sphere(transform=ScalingMatrix(0.5, 0.5, 0.5))')
def step_impl(context):
    context.s2 = Sphere(transform=ScalingMatrix(0.5, 0.5, 0.5))


@given('w ← default_world()')
def step_impl(context):
    context.w = default_world()


@given('shape ← the first object in w')
def step_impl(context):
    context.shape = context.w.shapes[0]


@given('w.light_source ← LightSource(Point(0, 0.25, 0), Color(1, 1, 1))')
def step_impl(context):
    context.w.light_source = LightSource(Point(0, 0.25, 0), Color(1, 1, 1))


@given('shape ← the second object in w')
def step_impl(context):
    context.shape = context.w.shapes[1]


@given('i ← Intersection(0.5, shape)')
def step_impl(context):
    context.i = Intersection(Decimal(0.5), context.shape)


@given('r ← Ray(Point(0, 0, -5), Vector(0, 1, 0))')
def step_impl(context):
    context.r = Ray(Point(0, 0, -5), Vector(0, 1, 0))


@given('outer ← the first object in w')
def step_impl(context):
    context.outer = context.w.shapes[0]


@given('outer.material.ambient ← 1')
def step_impl(context):
    context.outer.material.ambient = 1


@given('inner ← the second object in w')
def step_impl(context):
    context.inner = context.w.shapes[1]


@given('inner.material.ambient ← 1')
def step_impl(context):
    context.inner.material.ambient = 1


@given('r ← Ray(Point(0, 0, 0.75), Vector(0, 0, -1))')
def step_impl(context):
    context.r = Ray(Point(0, 0, 0.75), Vector(0, 0, -1))


@when('w ← default_world()')
def step_impl(context):
    context.w = default_world()


@when('xs ← w.intersect(r)')
def step_impl(context):
    context.xs = context.w.intersect(context.r)


@when('c ← w.shade_hit(comps)')
def step_impl(context):
    context.c = context.w.shade_hit(context.comps)


@when('c ← w.color_at(r)')
def step_impl(context):
    context.c = context.w.color_at(context.r)


@then('w contains no shapes')
def step_impl(context):
    assert len(context.w.shapes) == 0


@then('w has no light source')
def step_impl(context):
    assert context.w.light_source is None


@then('w.light_source = light_source')
def step_impl(context):
    assert context.w.light_source == context.light_source


@then('w contains s1')
def step_impl(context):
    assert context.s1 in context.w.shapes


@then('w contains s2')
def step_impl(context):
    assert context.s2 in context.w.shapes


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


@then('c = Color(0.38066, 0.47583, 0.2855)')
def step_impl(context):
    assert context.c == Color(0.38066, 0.47582, 0.28549)


@then('c = Color(0.90498, 0.90498, 0.90498)')
def step_impl(context):
    assert context.c == Color(0.90499, 0.90499, 0.90499)


@then(u'c = Color(0, 0, 0)')
def step_impl(context):
    assert context.c == Color(0, 0, 0)


@then(u'c = inner.material.color')
def step_impl(context):
    assert context.c == context.inner.material.color
