"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from decimal import Decimal

from behave import given, then, when

from src.color import Color
from src.matrix import Vector, Point

from src.scene import Material, LightPoint


@given('m ← Material()')
def step_impl(context):
    context.m = Material()


@given('eye_v ← Vector(0, 0, -1)')
def step_impl(context):
    context.eye_v = Vector(0, 0, -1)


@given('eye_v ← Vector(0, √2/2, -√2/2)')
def step_impl(context):
    context.eye_v = Vector(0, Decimal(2).sqrt() / 2, -Decimal(2).sqrt() / 2)


@given('eye_v ← Vector(0, -√2/2, -√2/2)')
def step_impl(context):
    context.eye_v = Vector(0, -Decimal(2).sqrt() / 2, -Decimal(2).sqrt() / 2)


@given('normal_v ← Vector(0, 0, -1)')
def step_impl(context):
    context.normal_v = Vector(0, 0, -1)


@given('light ← LightPoint(Point(0, 0, -10), Color(1, 1, 1))')
def step_impl(context):
    context.light = LightPoint(Point(0, 0, -10), Color(1, 1, 1))


@given('light ← LightPoint(Point(0, 10, -10), Color(1, 1, 1))')
def step_impl(context):
    context.light = LightPoint(Point(0, 10, -10), Color(1, 1, 1))


@given('light ← LightPoint(Point(0, 0, 10), Color(1, 1, 1))')
def step_impl(context):
    context.light = LightPoint(Point(0, 0, 10), Color(1, 1, 1))


@when('result ← m.lighting(light, position, eye_v, normal_v)')
def step_impl(context):
    context.result = context.m.lighting(context.light, context.position, context.eye_v, context.normal_v)


@when('result ← m.lighting(light, position, eye_v, normal_v, round_specular=False)')
def step_impl(context):
    context.result = context.m.lighting(context.light, context.position, context.eye_v, context.normal_v,
                                        round_specular=False)


@then('m.color = Color(1, 1, 1)')
def step_impl(context):
    assert context.m.color == Color(1, 1, 1)


@then('m.ambient = 0.1')
def step_impl(context):
    assert context.m.ambient == 0.1


@then('m.diffuse = 0.9')
def step_impl(context):
    assert context.m.diffuse == 0.9


@then('m.specular = 0.9')
def step_impl(context):
    assert context.m.specular == 0.9


@then('m.shininess = 200.0')
def step_impl(context):
    assert context.m.shininess == 200.0


@then('result = Color(1.9, 1.9, 1.9)')
def step_impl(context):
    assert context.result == Color(1.9, 1.9, 1.9)


@then('result = Color(1.0, 1.0, 1.0)')
def step_impl(context):
    assert context.result == Color(1.0, 1.0, 1.0)


@then('result = Color(0.7364, 0.7364, 0.7364)')
def step_impl(context):
    assert context.result == Color(0.7364, 0.7364, 0.7364)


@then('result = Color(1.6364, 1.6364, 1.6364)')
def step_impl(context):
    assert context.result == Color(1.6364, 1.6364, 1.6364)


@then('result = Color(1.6328, 1.6328, 1.6328)')
def step_impl(context):
    r = context.result
    assert context.result == Color(1.6328, 1.6328, 1.6328)


@then('result = Color(0.1, 0.1, 0.1)')
def step_impl(context):
    assert context.result == Color(0.1, 0.1, 0.1)
