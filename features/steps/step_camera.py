"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
import math
from decimal import Decimal

from behave import given, then, when

from src.camera import Camera
from src.color import Color
from src.matrix import IdentityMatrix, Point, Vector, RotationMatrix, TranslationMatrix


@given('h_size ← 160')
def step_impl(context):
    context.h_size = 160


@given('v_size ← 120')
def step_impl(context):
    context.v_size = 120


@given('field_of_view ← π/2')
def step_impl(context):
    context.field_of_view = math.pi / 2


@given('c ← Camera(200, 125, π/2)')
def step_impl(context):
    context.c = Camera(200, 125, Decimal(math.pi / 2))


@given('c ← Camera(125, 200, π/2)')
def step_impl(context):
    context.c = Camera(125, 200, Decimal(math.pi / 2))


@given('c ← Camera(201, 101, π/2)')
def step_impl(context):
    context.c = Camera(201, 101, Decimal(math.pi / 2))


@given('transform ← rotation_y(π/4) * translation(0, -2, 5)')
def step_impl(context):
    y_radians = math.pi / 4
    context.transform = RotationMatrix(y_radians=y_radians) * TranslationMatrix(0, -2, 5)


@given('c ← Camera(201, 101, π/2, transform)')
def step_impl(context):
    context.c = Camera(201, 101, Decimal(math.pi / 2), transform=context.transform)


@given('from ← Point(0, 0, -5)')
def step_impl(context):
    context.frm = Point(0, 0, -5)


@given('transform ← pov.transform()')
def step_impl(context):
    context.transform = context.pov.transform()


@given('c ← Camera(11, 11, π/2, transform)')
def step_impl(context):
    context.c = Camera(11, 11, Decimal(math.pi / 2), transform=context.transform)


@when('c ← Camera(h_size, v_size, field_of_view)')
def step_impl(context):
    context.c = Camera(context.h_size, context.v_size, context.field_of_view)


@when('r ← c.ray_for_pixel(100, 50)')
def step_impl(context):
    context.r = context.c.ray_for_pixel(100, 50)


@when('r ← c.ray_for_pixel(0, 0)')
def step_impl(context):
    context.r = context.c.ray_for_pixel(0, 0)


@when('canvas ← c.render(w)')
def step_impl(context):
    context.canvas = context.c.render(context.w)


@then('c.h_size = 160')
def step_impl(context):
    assert context.c.h_size == 160


@then('c.v_size = 120')
def step_impl(context):
    assert context.c.v_size == 120


@then('c.field_of_view = π/2')
def step_impl(context):
    assert context.c.field_of_view == math.pi / 2


@then('c.transform = IdentityMatrix()')
def step_impl(context):
    assert context.c.transform == IdentityMatrix()


@then('c.pixel_size = 0.01')
def step_impl(context):
    assert abs(context.c.pixel_size - Decimal('0.01')) < 0.00001


@then('r.origin = Point(0, 0, 0)')
def step_impl(context):
    assert context.r.origin == Point(0, 0, 0)


@then('r.direction = Vector(0, 0, -1)')
def step_impl(context):
    assert context.r.direction == Vector(0, 0, -1)


@then('r.direction = Vector(0.66519, 0.33259, -0.66851)')
def step_impl(context):
    assert context.r.direction == Vector(0.66519, 0.33259, -0.66851)


@then('r.origin = Point(0, 2, -5)')
def step_impl(context):
    assert context.r.origin == Point(0, 2, -5)


@then('r.direction = Vector(√2/2, 0, -√2/2)')
def step_impl(context):
    assert context.r.direction == Vector(math.sqrt(2) / 2, 0, -math.sqrt(2) / 2)


@then('canvas.pixel_at(5, 5) = Color(0.38066, 0.47583, 0.2855)')
def step_impl(context):
    p = context.canvas.pixel_at(5, 5)
    assert context.canvas.pixel_at(5, 5) == Color(0.38066, 0.47583, 0.2855)
