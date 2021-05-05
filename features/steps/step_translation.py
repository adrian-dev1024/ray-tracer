"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------

from behave import given, then

from src.coordinates import Point, Vector
from src.matrix import Translation


@given('transform ← Translation(5, -3, 2)')
def step_impl(context):
    context.transform = Translation(5, -3, 2)


@given('p ← Point(-3, 4, 5)')
def step_impl(context):
    context.p = Point(-3, 4, 5)

@given('inv ← transform.inverse()')
def step_impl(context):
    context.inv = context.transform.inverse()

@given('v ← Vector(-3, 4, 5)')
def step_impl(context):
    context.v = Vector(-3, 4, 5)

@then('transform * p = Point(2, 1, 7)')
def step_impl(context):
    assert context.transform * context.p == Point(2, 1, 7)

@then('inv * p = Point(-8, 7, 3)')
def step_impl(context):
    assert context.inv * context.p == Point(-8, 7, 3)

@then('transform * v = v')
def step_impl(context):
    assert context.transform * context.v == context.v
