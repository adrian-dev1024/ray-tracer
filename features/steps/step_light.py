"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------

from behave import given, then, when

from src.color import Color
from src.scene import LightPoint
from src.matrix import Point


@given('intensity ← Color(1, 1, 1)')
def step_impl(context):
    context.intensity = Color(1, 1, 1)


@given('position ← Point(0, 0, 0)')
def step_impl(context):
    context.position = Point(0, 0, 0)


@when('light ← LightPoint(position, intensity)')
def step_impl(context):
    context.light = LightPoint(context.position, context.intensity)


@then('light.position = position')
def step_impl(context):
    assert context.light.position == context.position


@then('light.intensity = intensity')
def step_impl(context):
    assert context.light.intensity == context.intensity
