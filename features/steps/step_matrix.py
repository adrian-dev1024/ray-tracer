"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
import itertools

from behave import given, then, when

from src.coordinates import Coordinate
from src.matrix import Matrix, IdentityMatrix


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


@given('the following 4x4 Matrix a')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.a = Matrix(4, 4, values=list(map(float, values)))


@given('the following 4x4 Matrix b')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.b = Matrix(4, 4, values=list(map(float, values)))


@given('the following 2x3 Matrix a')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.a = Matrix(2, 3, values=list(map(float, values)))


@given('the following 3x2 Matrix b')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.b = Matrix(3, 2, values=list(map(float, values)))


@given('b ← Coordinate(1, 2, 3, 1)')
def step_impl(context):
    context.b = Coordinate(1, 2, 3, 1)


@given('a ← Coordinate(1, 2, 3, 4)')
def step_impl(context):
    context.a = Coordinate(1, 2, 3, 4)


@given('a ← identity_matrix.transpose()')
def step_impl(context):
    context.a = IdentityMatrix.transpose()


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
    assert context.a.__eq__(context.b)


@then('a != b')
def step_impl(context):
    assert context.a != context.b


@then('a * b is the following 4x4 Matrix')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    assert context.a * context.b == Matrix(4, 4, values=list(map(float, values)))


@then('a * b is the following 2x2 Matrix')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    assert context.a * context.b == Matrix(2, 2, values=list(map(float, values)))


@then('a * b = Coordinate(18, 24, 33, 1)')
def step_impl(context):
    assert context.a * context.b == Coordinate(18, 24, 33, 1)


@then('a * identity_matrix = a')
def step_impl(context):
    assert context.a * IdentityMatrix == context.a


@then('identity_matrix * a = a')
def step_impl(context):
    assert IdentityMatrix * context.a == context.a


@then('a.transpose() is the following matrix')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    assert context.a.transpose() == Matrix(4, 4, values=list(map(float, values)))


@then('a = identity_matrix')
def step_impl(context):
    assert context.a == IdentityMatrix
