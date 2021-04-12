"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, then, when

from src.canvas import Canvas
from src.color import Color


@given('c ← Canvas(10, 20)')
def step_impl(context):
    context.c = Canvas(10, 20)


@given('red ← Color(1, 0, 0)')
def step_impl(context):
    context.red = Color(1, 0, 0)


@when('c.write_pixel(2, 3, red)')
def step_impl(context):
    context.c.write_pixel(2, 3, context.red)


@then('c.width = 10')
def step_impl(context):
    assert context.c.width == 10


@then('c.height = 20')
def step_impl(context):
    assert context.c.height == 20


@then('every pixel of c is Color(0, 0, 0)')
def step_impl(context):
    black = Color(0, 0, 0)
    valid = True
    for inner in context.c.grid:
        for color in inner:
            valid = color == black
            if not valid:
                break
        if not valid:
            break
    assert valid


@then('c.pixel_at(2, 3) = red')
def step_impl(context):
    assert context.c.pixel_at(2, 3) == context.red
