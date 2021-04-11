"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------

from behave import given, then

from src.color import Color


@given('c ← Color(-0.5, 0.4, 1.7)')
def step_impl(context):
    context.c = Color(-0.5, 0.4, 1.7)


@then('c.red = -0.5')
def step_impl(context):
    assert context.c.red == -0.5


@then('c.green = 0.4')
def step_impl(context):
    assert context.c.green == 0.4


@then('c.blue = 1.7')
def step_impl(context):
    assert context.c.blue == 1.7
