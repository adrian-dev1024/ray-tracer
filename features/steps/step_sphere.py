"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------

from behave import given, then, when

from src.matrix import Point, Vector
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


@when('xs ← s.intersect(r)')
def step_impl(context):
    context.xs = context.s.intersect(context.r)


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
