"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------

from behave import given, then, when

from src.matrix import Point, Vector, ScalingMatrix, TranslationMatrix
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


@given('r ← Ray(Point(1, 2, 3), Vector(0, 1, 0))')
def step_impl(context):
    context.r = Ray(Point(1, 2, 3), Vector(0, 1, 0))


@given('m ← TranslationMatrix(3, 4, 5)')
def step_impl(context):
    context.m = TranslationMatrix(3, 4, 5)


@given('m ← ScalingMatrix(2, 3, 4)')
def step_impl(context):
    context.m = ScalingMatrix(2, 3, 4)


@when('r ← Ray(origin, direction)')
def step_impl(context):
    context.r = Ray(context.origin, context.direction)


@when('r2 ← r.transform(m)')
def step_impl(context):
    context.r2 = context.r.transform(context.m)


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


@then('r2.origin = Point(4, 6, 8)')
def step_impl(context):
    assert context.r2.origin == Point(4, 6, 8)


@then('r2.direction = Vector(0, 1, 0)')
def step_impl(context):
    assert context.r2.direction == Vector(0, 1, 0)


@then('r2.origin = Point(2, 6, 12)')
def step_impl(context):
    assert context.r2.origin == Point(2, 6, 12)


@then('r2.direction = Vector(0, 3, 0)')
def step_impl(context):
    assert context.r2.direction == Vector(0, 3, 0)
