"""
Scenario: A Coordinate with w=1.0 is a point
  Given a ← tuple(4.3, -4.2, 3.1, 1.0)
  Then a.x = 4.3
    And a.y = -4.2
    And a.z = 3.1
    And a.w = 1.0
    And a is a point
    And a is not a vector

Scenario: A Coordinate with w=0 is a vector
  Given a ← Coordinate(4.3, -4.2, 3.1, 0.0)
  Then a.x = 4.3
    And a.y = -4.2
    And a.z = 3.1
    And a.w = 0.0
    And a is not a point
    And a is a vector
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, then

from src.coordinates import Coordinate, is_a_point, is_a_vector, Point, Vector


@given('a ← Coordinate(4.3, -4.2, 3.1, 1.0)')
def step_impl(context):
    context.a = Coordinate(4.3, -4.2, 3.1, 1.0)


@given('b ← Coordinate(4.3, -4.2, 3.1, 0.0)')
def step_impl(context):
    context.b = Coordinate(4.3, -4.2, 3.1, 0.0)


@given('p ← Point(4, -4, 3)')
def step_impl(context):
    context.p = Point(4, -4, 3)


@given('v ← Vector(4, -4, 3)')
def step_impl(context):
    context.v = Vector(4, -4, 3)


@then('a.x = 4.3')
def step_impl(context):
    assert context.a.x == 4.3


@then('a.y = -4.2')
def step_impl(context):
    assert context.a.y == -4.2


@then('a.z = 3.1')
def step_impl(context):
    assert context.a.z == 3.1


@then('a.w = 1.0')
def step_impl(context):
    assert context.a.w == 1.0


@then('a is a point')
def step_impl(context):
    assert is_a_point(context.a)


@then('a is not a vector')
def step_impl(context):
    assert not is_a_vector(context.a)


@then('b.x = 4.3')
def step_impl(context):
    assert context.b.x == 4.3


@then('b.y = -4.2')
def step_impl(context):
    assert context.b.y == -4.2


@then('b.z = 3.1')
def step_impl(context):
    assert context.b.z == 3.1


@then('b.w = 0.0')
def step_impl(context):
    assert context.b.w == 0.0


@then('b is not a point')
def step_impl(context):
    assert not is_a_point(context.b)


@then('b is a vector')
def step_impl(context):
    assert is_a_vector(context.b)


@then('p = Coordinate(4, -4, 3, 1)')
def step_impl(context):
    assert context.p.coordinate == Coordinate(4, -4, 3, 1)


@then('v = Coordinate(4, -4, 3, 0)')
def step_impl(context):
    assert context.v.coordinate == Coordinate(4, -4, 3, 0)
