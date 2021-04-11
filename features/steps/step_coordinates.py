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

Scenario: Point() creates tuples with w=1
  Given p ← Point(4, -4, 3)
  Then p = Coordinate(4, -4, 3, 1)

Scenario: Vector() creates tuples with w=0
  Given v ← Vector(4, -4, 3)
  Then v = Coordinate(4, -4, 3, 0)
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
import math

from behave import given, then, when

from src.coordinates import Coordinate, Point, Vector


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


@given('a1 ← Coordinate(3, -2, 5, 1)')
def step_impl(context):
    context.a1 = Coordinate(3, -2, 5, 1)


@given('a2 ← Coordinate(-2, 3, 1, 0)')
def step_impl(context):
    context.a2 = Coordinate(-2, 3, 1, 0)


@given('p1 ← Point(3, 2, 1)')
def step_impl(context):
    context.p1 = Point(3, 2, 1)


@given('p2 ← Point(5, 6, 7)')
def step_impl(context):
    context.p2 = Point(5, 6, 7)


@given('v1 ← Vector(3, 2, 1)')
def step_impl(context):
    context.v1 = Vector(3, 2, 1)


@given('v2 ← Vector(5, 6, 7)')
def step_impl(context):
    context.v2 = Vector(5, 6, 7)


@given('zero ← Vector(0, 0, 0)')
def step_impl(context):
    context.zero = Vector(0, 0, 0)


@given('v ← Vector(1, -2, 3)')
def step_impl(context):
    context.v = Vector(1, -2, 3)


@given('a ← Coordinate(1, -2, 3, -4)')
def step_impl(context):
    context.a = Coordinate(1, -2, 3, -4)


@given('v ← Vector(1, 0, 0)')
def step_impl(context):
    context.v = Vector(1, 0, 0)


@given('v ← Vector(0, 1, 0)')
def step_impl(context):
    context.v = Vector(0, 1, 0)


@given('v ← Vector(0, 0, 1)')
def step_impl(context):
    context.v = Vector(0, 0, 1)


@given('v ← Vector(1, 2, 3)')
def step_impl(context):
    context.v = Vector(1, 2, 3)


@given('v ← Vector(-1, -2, -3)')
def step_impl(context):
    context.v = Vector(-1, -2, -3)


@given('v ← Vector(4, 0, 0)')
def step_impl(context):
    context.v = Vector(4, 0, 0)


@given('a ← Vector(1, 2, 3)')
def step_impl(context):
    context.a = Vector(1, 2, 3)


@given('b ← Vector(2, 3, 4)')
def step_impl(context):
    context.b = Vector(2, 3, 4)


@when('norm ← v.normalize()')
def step_impl(context):
    context.norm = context.v.normalize()


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
    assert context.a.is_a_point()


@then('a is not a vector')
def step_impl(context):
    assert not context.a.is_a_vector()


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
    assert not context.b.is_a_point()


@then('b is a vector')
def step_impl(context):
    assert context.b.is_a_vector()


@then('p = Coordinate(4, -4, 3, 1)')
def step_impl(context):
    assert context.p == Coordinate(4, -4, 3, 1)


@then('v = Coordinate(4, -4, 3, 0)')
def step_impl(context):
    assert context.v == Coordinate(4, -4, 3, 0)


@then('a1 + a2 = Coordinate(1, 1, 6, 1)')
def step_impl(context):
    assert context.a1 + context.a2 == Coordinate(1, 1, 6, 1)


@then('p1 - p2 = Vector(-2, -4, -6)')
def step_impl(context):
    assert context.p1 - context.p2 == Vector(-2, -4, -6)


@then('p1 - v2 = Point(-2, -4, -6)')
def step_impl(context):
    assert context.p1 - context.v2 == Point(-2, -4, -6)


@then('v1 - v2 = Vector(-2, -4, -6)')
def step_impl(context):
    assert context.v1 - context.v2 == Vector(-2, -4, -6)


@then('zero - v = Vector(-1, 2, -3)')
def step_impl(context):
    assert context.zero - context.v == Vector(-1, 2, -3)


@then('-a = Coordinate(-1, 2, -3, 4)')
def step_impl(context):
    assert -context.a == Coordinate(-1, 2, -3, 4)


@then('a * 3.5 = Coordinate(3.5, -7, 10.5, -14)')
def step_impl(context):
    assert context.a * 3.5 == Coordinate(3.5, -7, 10.5, -14)


@then('a * 0.5 = Coordinate(0.5, -1, 1.5, -2)')
def step_impl(context):
    assert context.a * 0.5 == Coordinate(0.5, -1, 1.5, -2)


@then('a / 2 = Coordinate(0.5, -1, 1.5, -2)')
def step_impl(context):
    assert context.a / 2 == Coordinate(0.5, -1, 1.5, -2)


@then('v.magnitude() = 1')
def step_impl(context):
    assert context.v.magnitude() == 1


@then('v.magnitude() = √14')
def step_impl(context):
    assert context.v.magnitude() == math.sqrt(14)


@then('v.normalize() = Vector(1, 0, 0)')
def step_impl(context):
    assert context.v.normalize() == Vector(1, 0, 0)


@then('v.normalize() = approximately Vector(0.26726, 0.53452, 0.80178)')
def step_impl(context):
    norm = context.v.normalize()
    assert math.isclose(norm.x, 0.26726, rel_tol=0.00001)
    assert math.isclose(norm.y, 0.53452, rel_tol=0.00001)
    assert math.isclose(norm.z,  0.80178, rel_tol=0.00001)


@then('v.normalize() = Vector(1/√14, 2/√14, 3/√14)')
def step_impl(context):
    assert context.v.normalize() == Vector(1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14))


@then('norm.magnitude() = 1')
def step_impl(context):
    assert context.norm.magnitude() == 1


@then('a.dot(b) = 20')
def step_impl(context):
    assert context.a.dot(context.b) == 20


@then('a.cross(b) = Vector(-1, 2, -1)')
def step_impl(context):
    assert context.a.cross(context.b) == Vector(-1, 2, -1)


@then('b.cross(a) = Vector(1, -2, 1)')
def step_impl(context):
    assert context.b.cross(context.a) == Vector(1, -2, 1)




