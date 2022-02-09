"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
import itertools
from decimal import Decimal

from behave import given, then, when
import math

from src.matrix import TranslationMatrix, ScalingMatrix, RotationMatrix, ShearingMatrix, Point, Vector, IdentityMatrix, \
    Matrix
from src.scene import PointOfView


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


@given('p ← Point(1, 0, 1)')
def step_impl(context):
    context.p = Point(1, 0, 1)


@when('p2 ← p.rotate(x_radians=π / 2)')
def step_impl(context):
    context.p2 = context.p.rotate(x_radians=Decimal(math.pi) / 2)


@when('p3 ← p2.scale(5, 5, 5)')
def step_impl(context):
    context.p3 = context.p2.scale(5, 5, 5)


@when('p4 ← p3.translate(10, 5, 7)')
def step_impl(context):
    context.p4 = context.p3.translate(10, 5, 7)


@when('p2 ← p.rotate(x_radians=π / 2).scale(5, 5, 5).translate(10, 5, 7)')
def step_impl(context):
    context.p2 = context.p.rotate(x_radians=Decimal(math.pi) / 2).scale(5, 5, 5).translate(10, 5, 7)


@given('transform ← ShearingMatrix(x_y=1)')
def step_impl(context):
    context.transform = ShearingMatrix(x_y=1)


@given('transform ← ShearingMatrix(x_z=1)')
def step_impl(context):
    context.transform = ShearingMatrix(x_z=1)


@given('transform ← ShearingMatrix(y_x=1)')
def step_impl(context):
    context.transform = ShearingMatrix(y_x=1)


@given('transform ← ShearingMatrix(y_z=1)')
def step_impl(context):
    context.transform = ShearingMatrix(y_z=1)


@given('transform ← ShearingMatrix(z_x=1)')
def step_impl(context):
    context.transform = ShearingMatrix(z_x=1)


@given('transform ← ShearingMatrix(z_y=1)')
def step_impl(context):
    context.transform = ShearingMatrix(z_y=1)


@given('from ← Point(0, 0, 0)')
def step_impl(context):
    context.frm = Point(0, 0, 0)


@given('to ← Point(0, 0, -1)')
def step_impl(context):
    context.to = Point(0, 0, -1)


@given('up ← Vector(0, 1, 0)')
def step_impl(context):
    context.up = Vector(0, 1, 0)


@given('pov ← PointOfView(from, to, up)')
def step_impl(context):
    context.pov = PointOfView(context.frm, context.to, context.up)


@given('to ← Point(0, 0, 1)')
def step_impl(context):
    context.to = Point(0, 0, 1)


@given('from ← Point(0, 0, 8)')
def step_impl(context):
    context.frm = Point(0, 0, 8)


@given('to ← Point(0, 0, 0)')
def step_impl(context):
    context.to = Point(0, 0, 0)


@when('t ← pov.transform()')
def step_impl(context):
    context.t = context.pov.transform()


@given('from ← Point(1, 3, 2)')
def step_impl(context):
    context.frm = Point(1, 3, 2)


@given(u'to ← Point(4, -2, 8)')
def step_impl(context):
    context.to = Point(4, -2, 8)


@given('up ← Vector(1, 1, 0)')
def step_impl(context):
    context.up = Vector(1, 1, 0)


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


@then('p2 = Point(1, -1, 0)')
def step_impl(context):
    assert context.p2 == Point(1, -1, 0)


@then('p3 = Point(5, -5, 0)')
def step_impl(context):
    assert context.p3 == Point(5, -5, 0)


@then('p4 = Point(15, 0, 7)')
def step_impl(context):
    assert context.p4 == Point(15, 0, 7)


@then('p2 = Point(15, 0, 7)')
def step_impl(context):
    assert context.p2 == Point(15, 0, 7)


@then('transform * p = Point(5, 3, 4)')
def step_impl(context):
    assert context.transform * context.p == Point(5, 3, 4)


@then('transform * p = Point(6, 3, 4)')
def step_impl(context):
    assert context.transform * context.p == Point(6, 3, 4)


@then('transform * p = Point(2, 5, 4)')
def step_impl(context):
    assert context.transform * context.p == Point(2, 5, 4)


@then('transform * p = Point(2, 7, 4)')
def step_impl(context):
    assert context.transform * context.p == Point(2, 7, 4)


@then('transform * p = Point(2, 3, 6)')
def step_impl(context):
    assert context.transform * context.p == Point(2, 3, 6)


@then('transform * p = Point(2, 3, 7)')
def step_impl(context):
    assert context.transform * context.p == Point(2, 3, 7)


@then('t = IdentityMatrix()')
def step_impl(context):
    assert context.t == IdentityMatrix()


@then('t = ScalingMatrix(-1, 1, -1)')
def step_impl(context):
    assert context.t == ScalingMatrix(-1, 1, -1)


@then('t = TranslationMatrix(0, 0, -8)')
def step_impl(context):
    assert context.t == TranslationMatrix(0, 0, -8)


@then('t is the following 4x4 matrix')
def step_impl(context):
    t = context.t
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    a = Matrix(4, 4, values=list(map(Decimal, values)))
    assert context.t == Matrix(4, 4, values=list(map(Decimal, values)))
