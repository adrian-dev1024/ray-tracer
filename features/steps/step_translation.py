"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from decimal import Decimal

from behave import given, then
import math

from src.coordinates import Point, Vector
from src.matrix import TranslationMatrix, ScalingMatrix, RotationMatrix


@given('transform ← TranslationMatrix(5, -3, 2)')
def step_impl(context):
    context.transform = TranslationMatrix(5, -3, 2)


@given('p ← Point(-3, 4, 5)')
def step_impl(context):
    context.p = Point(-3, 4, 5)


@given('inv ← transform.inverse()')
def step_impl(context):
    context.inv = context.transform.inverse()


@given('transform ← ScalingMatrix(2, 3, 4)')
def step_impl(context):
    context.transform = ScalingMatrix(2, 3, 4)


@given('p ← Point(-4, 6, 8)')
def step_impl(context):
    context.p = Point(-4, 6, 8)


@given('v ← Vector(-4, 6, 8)')
def step_impl(context):
    context.v = Vector(-4, 6, 8)


@given('v ← Vector(-3, 4, 5)')
def step_impl(context):
    context.v = Vector(-3, 4, 5)


@given('transform ← ScalingMatrix(-1, 1, 1)')
def step_impl(context):
    context.transform = ScalingMatrix(-1, 1, 1)


@given('p ← Point(2, 3, 4)')
def step_impl(context):
    context.p = Point(2, 3, 4)


@given('p ← Point(0, 1, 0)')
def step_impl(context):
    context.p = Point(0, 1, 0)


@given('half_quarter ← RotationMatrix(x_radians=π / 4)')
def step_impl(context):
    context.half_quarter = RotationMatrix(x_radians=Decimal(math.pi) / 4)


@given('full_quarter ← RotationMatrix(x_radians=π / 2)')
def step_impl(context):
    context.full_quarter = RotationMatrix(x_radians=Decimal(math.pi) / 2)


@given('inv ← half_quarter.inverse()')
def step_impl(context):
    context.inv = context.half_quarter.inverse()


@given('p ← Point(0, 0, 1)')
def step_impl(context):
    context.p = Point(0, 0, 1)


@given('half_quarter ← RotationMatrix(y_radians=π / 4)')
def step_impl(context):
    context.half_quarter = RotationMatrix(y_radians=Decimal(math.pi) / 4)


@given('full_quarter ← RotationMatrix(y_radians=π / 2)')
def step_impl(context):
    context.full_quarter = RotationMatrix(y_radians=Decimal(math.pi) / 2)


@given('half_quarter ← RotationMatrix(z_radians=π / 4)')
def step_impl(context):
    context.half_quarter = RotationMatrix(z_radians=Decimal(math.pi) / 4)


@given('full_quarter ← RotationMatrix(z_radians=π / 2)')
def step_impl(context):
    context.full_quarter = RotationMatrix(z_radians=Decimal(math.pi) / 2)


@then('transform * p = Point(2, 1, 7)')
def step_impl(context):
    assert context.transform * context.p == Point(2, 1, 7)


@then('inv * p = Point(-8, 7, 3)')
def step_impl(context):
    assert context.inv * context.p == Point(-8, 7, 3)


@then('transform * v = v')
def step_impl(context):
    assert context.transform * context.v == context.v


@then('transform * p = Point(-8, 18, 32)')
def step_impl(context):
    assert context.transform * context.p == Point(-8, 18, 32)


@then('transform * v = Vector(-8, 18, 32)')
def step_impl(context):
    assert context.transform * context.v == Vector(-8, 18, 32)


@then('inv * v = Vector(-2, 2, 2)')
def step_impl(context):
    assert context.inv * context.v == Vector(-2, 2, 2)


@then('transform * p = Point(-2, 3, 4)')
def step_impl(context):
    assert context.transform * context.p == Point(-2, 3, 4)


@then('half_quarter * p = Point(0, √2/2, √2/2)')
def step_impl(context):
    assert context.half_quarter * context.p == Point(0, Decimal(math.sqrt(2)) / 2, Decimal(math.sqrt(2)) / 2)


@then('full_quarter * p = Point(0, 0, 1)')
def step_impl(context):
    assert context.full_quarter * context.p == Point(0, 0, 1)


@then('inv * p = Point(0, √2/2, -√2/2)')
def step_impl(context):
    assert context.half_quarter * context.p == Point(0, Decimal(math.sqrt(2)) / 2, Decimal(math.sqrt(2)) / 2)


@then('half_quarter * p = Point(√2/2, 0, √2/2)')
def step_impl(context):
    assert context.half_quarter * context.p == Point(Decimal(math.sqrt(2)) / 2, 0, Decimal(math.sqrt(2)) / 2)


@then('full_quarter * p = Point(1, 0, 0)')
def step_impl(context):
    assert context.full_quarter * context.p == Point(1, 0, 0)


@then('half_quarter * p = Point(-√2/2, √2/2, 0)')
def step_impl(context):
    assert context.half_quarter * context.p == Point(Decimal(-math.sqrt(2)) / 2, Decimal(math.sqrt(2)) / 2, 0)


@then('full_quarter * p = Point(-1, 0, 0)')
def step_impl(context):
    assert context.full_quarter * context.p == Point(-1, 0, 0)
