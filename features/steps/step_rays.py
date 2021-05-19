"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------

from behave import given, then, when

from src.matrix import Point, Vector
from src.ray import Ray


@given('origin ← Point(1, 2, 3)')
def step_impl(context):
    context.origin = Point(1, 2, 3)


@given('direction ← Vector(4, 5, 6)')
def step_impl(context):
    context.direction = Vector(4, 5, 6)


@given('r ← Ray(Point(2, 3, 4), Vector(1, 0, 0))')
def step_impl(context):
    context.r = Ray(Point(2, 3, 4), Vector(1, 0, 0))


@when('r ← Ray(origin, direction)')
def step_impl(context):
    context.r = Ray(context.origin, context.direction)


@then('r.origin = origin')
def step_impl(context):
    assert context.r.origin == context.origin


@then('r.direction = direction')
def step_impl(context):
    assert context.r.direction == context.direction


@then('r.position(0) = Point(2, 3, 4)')
def step_impl(context):
    assert context.r.position(0) == Point(2, 3, 4)


@then('r.position(1) = Point(3, 3, 4)')
def step_impl(context):
    assert context.r.position(1) == Point(3, 3, 4)


@then('r.position(-1) = Point(1, 3, 4)')
def step_impl(context):
    assert context.r.position(-1) == Point(1, 3, 4)


@then('r.position(2.5) = Point(4.5, 3, 4)')
def step_impl(context):
    assert context.r.position(2.5) == Point(4.5, 3, 4)
