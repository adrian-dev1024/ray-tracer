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


@given('c ← Canvas(5, 3)')
def step_impl(context):
    context.c = Canvas(5, 3)


@given('c1 ← Color(1.5, 0, 0)')
def step_impl(context):
    context.c1 = Color(1.5, 0, 0)


@given('c2 ← Color(0, 0.5, 0)')
def step_impl(context):
    context.c2 = Color(0, 0.5, 0)


@given('c3 ← Color(-0.5, 0, 1)')
def step_impl(context):
    context.c3 = Color(-0.5, 0, 1)


@given('c ← Canvas(10, 2)')
def step_impl(context):
    context.c = Canvas(10, 2)


@when('c.write_pixel(2, 3, red)')
def step_impl(context):
    context.c.write_pixel(2, 3, context.red)


@when('c.write_pixel(0, 0, c1)')
def step_impl(context):
    context.c.write_pixel(0, 0, context.c1)


@when('c.write_pixel(2, 1, c2)')
def step_impl(context):
    context.c.write_pixel(2, 1, context.c2)


@when('c.write_pixel(4, 2, c3)')
def step_impl(context):
    context.c.write_pixel(4, 2,  context.c3)


@when('every pixel of c is set to Color(1, 0.8, 0.6)')
def step_impl(context):
    color = Color(1, 0.8, 0.6)
    for y in range(2):
        for x in range(10):
            context.c.write_pixel(x, y,  color)


@when('ppm ← c.to_ppm()')
def step_impl(context):
    context.ppm = context.c.to_ppm()


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


@then('lines 1-3 of ppm are')
def step_impl(context):
    """
    P3
    5 3
    255
    """
    header = 'P3\n5 3\n255\n'
    assert context.ppm.startswith(header)


@then('lines 4-6 of ppm are')
def step_impl(context):
    """
    255 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 128 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 255
    """
    body = '255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n'
    body += '0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n'
    body += '0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n'
    p = context.ppm
    assert context.ppm.endswith(body)


@then('lines 4-7 of ppm are')
def step_impl(context):
    """
    255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
    153 255 204 153 255 204 153 255 204 153 255 204 153
    255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
    153 255 204 153 255 204 153 255 204 153 255 204 153
    """
    body = '255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n'
    body += '153 255 204 153 255 204 153 255 204 153 255 204 153\n'
    body += '255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n'
    body += '153 255 204 153 255 204 153 255 204 153 255 204 153\n'
    assert context.ppm.endswith(body)


@then('ppm ends with a newline character')
def step_impl(context):
    assert context.ppm.endswith('\n')
