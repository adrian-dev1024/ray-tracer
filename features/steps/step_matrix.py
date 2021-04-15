"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
import itertools

from behave import given, then, when

from src.matrix import Matrix


@given('the following 4x4 Matrix m')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.m = Matrix(4, 4, values=list(map(float, values)))


@given('the following 2x2 Matrix m')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.m = Matrix(2, 2, values=list(map(float, values)))


@given('the following 3x3 Matrix m')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.m = Matrix(3, 3, values=list(map(float, values)))


@given('the following Matrix a')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.a = Matrix(4, 4, values=list(map(float, values)))


@given('the following Matrix b')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.b = Matrix(4, 4, values=list(map(float, values)))


@then('m[0,0] = 1')
def step_impl(context):
    assert context.m[0, 0] == 1


@then('m[0,3] = 4')
def step_impl(context):
    assert context.m[0, 3] == 4


@then('m[1,0] = 5.5')
def step_impl(context):
    assert context.m[1, 0] == 5.5


@then('m[1,2] = 7.5')
def step_impl(context):
    assert context.m[1, 2] == 7.5


@then('m[2,2] = 11')
def step_impl(context):
    assert context.m[2, 2] == 11


@then('m[3,0] = 13.5')
def step_impl(context):
    assert context.m[3, 0] == 13.5


@then('m[3,2] = 15.5')
def step_impl(context):
    assert context.m[3, 2] == 15.5


@then('m[0,0] = -3')
def step_impl(context):
    assert context.m[0, 0] == -3


@then('m[0,1] = 5')
def step_impl(context):
    assert context.m[0, 1] == 5


@then('m[1,0] = 1')
def step_impl(context):
    assert context.m[1, 0] == 1


@then('m[1,1] = -2')
def step_impl(context):
    assert context.m[1, 1] == -2


@then('m[2,2] = 1')
def step_impl(context):
    assert context.m[2, 2] == 1


@then('a = b')
def step_impl(context):
    a = context.a
    b = context.b
    e = a == b
    e1 = a.__eq__(b)
    assert context.a.__eq__(context.b)


@then('a != b')
def step_impl(context):
    assert context.a != context.b
