"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from decimal import Decimal

from behave import given, then, when

from src.intersection import Intersection, Intersections


@given('i1 ← Intersection(1, s)')
def step_impl(context):
    context.i1 = Intersection(Decimal(1), context.s)


@given('i2 ← Intersection(2, s)')
def step_impl(context):
    context.i2 = Intersection(Decimal(2), context.s)


@when('i ← Intersection(3.5, s)')
def step_impl(context):
    context.i = Intersection(Decimal(3.5), context.s)


@when('xs ← Intersections(i1, i2)')
def step_impl(context):
    context.xs = Intersections(context.i1, context.i2)


@then('i.t = 3.5')
def step_impl(context):
    assert context.i.t == 3.5


@then('i.obj = s')
def step_impl(context):
    assert context.i.obj == context.s


@then('xs[0].t = 1')
def step_impl(context):
    assert context.xs[0].t == 1


@then('xs[1].t = 2')
def step_impl(context):
    assert context.xs[1].t == 2
