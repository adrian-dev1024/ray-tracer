"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from decimal import Decimal

from behave import given, then

from src.color import Color


@given('c ← Color(-0.5, 0.4, 1.7)')
def step_impl(context):
    context.c = Color(-0.5, 0.4, 1.7)


@given('c1 ← Color(0.9, 0.6, 0.75)')
def step_impl(context):
    context.c1 = Color(0.9, 0.6, 0.75)


@given('c2 ← Color(0.7, 0.1, 0.25)')
def step_impl(context):
    context.c2 = Color(0.7, 0.1, 0.25)


@given('c1 ← Color(1, 0.2, 0.4)')
def step_impl(context):
    context.c1 = Color(1, 0.2, 0.4)


@given('c2 ← Color(0.9, 1, 0.1)')
def step_impl(context):
    context.c2 = Color(0.9, 1, 0.1)


@given('c ← Color(0.2, 0.3, 0.4)')
def step_impl(context):
    context.c = Color(0.2, 0.3, 0.4)


@then('c.red = -0.5')
def step_impl(context):
    assert context.c.red == Decimal(str(-0.5))


@then('c.green = 0.4')
def step_impl(context):
    assert abs(context.c.green - Decimal(str(0.4))) < 0.000001


@then('c.blue = 1.7')
def step_impl(context):
    assert abs(context.c.blue - Decimal(str(1.7))) < 0.000001


@then('c1 + c2 = Color(1.6, 0.7, 1.0)')
def step_impl(context):
    assert context.c1 + context.c2 == Color(1.6, 0.7, 1.0)


@then('c1 - c2 = Color(0.2, 0.5, 0.5)')
def step_impl(context):
    assert context.c1 - context.c2 == Color(0.2, 0.5, 0.5)


@then('c * 2 = Color(0.4, 0.6, 0.8)')
def step_impl(context):
    assert context.c * 2 == Color(0.4, 0.6, 0.8)


@then('c1 * c2 = Color(0.9, 0.2, 0.04)')
def step_impl(context):
    assert context.c1 * context.c2 == Color(0.9, 0.2, 0.04)
