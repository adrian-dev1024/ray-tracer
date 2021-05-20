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

@given('i1 ← Intersection(-1, s)')
def step_impl(context):
    context.i1 = Intersection(Decimal(-1), context.s)


@given('i2 ← Intersection(1, s)')
def step_impl(context):
    context.i2 = Intersection(Decimal(1), context.s)

@given('i1 ← Intersection(-2, s)')
def step_impl(context):
    context.i1 = Intersection(Decimal(-2), context.s)


@given('i2 ← Intersection(-1, s)')
def step_impl(context):
    context.i2 = Intersection(Decimal(-1), context.s)

@given('i1 ← Intersection(5, s)')
def step_impl(context):
    context.i1 = Intersection(Decimal(5), context.s)

@given('i2 ← Intersection(7, s)')
def step_impl(context):
    context.i2 = Intersection(Decimal(7), context.s)

@given('i3 ← Intersection(-3, s)')
def step_impl(context):
    context.i3 = Intersection(Decimal(-3), context.s)

@given('i4 ← Intersection(2, s)')
def step_impl(context):
    context.i4 = Intersection(Decimal(2), context.s)


@given('xs ← Intersections(i2, i1)')
def step_impl(context):
    context.xs = Intersections(context.i2, context.i1)

@given('xs ← Intersections(i1, i2, i3, i4)')
def step_impl(context):
    context.xs = Intersections(context.i1, context.i2, context.i3, context.i4)


@when('i ← Intersection(3.5, s)')
def step_impl(context):
    context.i = Intersection(Decimal(3.5), context.s)


@when('xs ← Intersections(i1, i2)')
def step_impl(context):
    context.xs = Intersections(context.i1, context.i2)


@when('i ← xs.hit()')
def step_impl(context):
    context.i = context.xs.hit()


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


@then('i = i1')
def step_impl(context):
    assert context.i == context.i1


@then('i = i2')
def step_impl(context):
    assert context.i == context.i2


@then('i is nothing')
def step_impl(context):
    assert context.i == None


@then('i = i4')
def step_impl(context):
    assert context.i == context.i4