"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------

from behave import given, then

from src.color import Color

from src.scene import Material


@given('m ← Material()')
def step_impl(context):
    context.m = Material()


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
