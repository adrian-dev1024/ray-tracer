"""

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
import itertools
from decimal import Decimal

from behave import given, then

from src.matrix import Matrix, IdentityMatrix, Scalar


# getcontext().prec = 6

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


@given('b ← Scalar(1, 2, 3, 1)')
def step_impl(context):
    context.b = Scalar(1, 2, 3, 1)


@given('a ← Scalar(1, 2, 3, 4)')
def step_impl(context):
    context.a = Scalar(1, 2, 3, 4)


@given('a ← identity_matrix of "{size}"')
def step_impl(context, size):
    context.a = IdentityMatrix(int(size))


@given('b ← a.transpose()')
def step_impl(context):
    context.b = context.a.transpose()


@given('the following 2x2 Matrix a')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.a = Matrix(2, 2, values=list(map(float, values)))


@given('the following 3x3 Matrix a')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    context.a = Matrix(3, 3, values=list(map(float, values)))


@given('b ← a.sub_matrix(1, 0)')
def step_impl(context):
    context.b = context.a.sub_matrix(1, 0)


@given('b ← a.inverse() identity_matrix')
def step_impl(context):
    context.b = context.a.inverse()


@given('b ← a.inverse()')
def step_impl(context):
    context.b = context.a.inverse()


@given('c ← a * b')
def step_impl(context):
    context.c = context.a * context.b


@given('identity_matrix of size 4x4')
def step_impl(context):
    context.identity_matrix = IdentityMatrix(4)


@given('inverse ← a.inverse()')
def step_impl(context):
    context.inverse = context.a.inverse()


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


@then('a * b = Scalar(18, 24, 33, 1)')
def step_impl(context):
    assert context.a * context.b == Scalar(18, 24, 33, 1)


@then('a * identity_matrix = a')
def step_impl(context):
    assert context.a * context.identity_matrix == context.a


@then('identity_matrix * a = a')
def step_impl(context):
    assert context.identity_matrix * context.a == context.a


@then('a.transpose() is the following matrix')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    assert context.a.transpose() == Matrix(4, 4, values=list(map(float, values)))


@then('a = identity_matrix')
def step_impl(context):
    assert context.a == IdentityMatrix


@then('a.determinant() = 17')
def step_impl(context):
    assert context.a.determinant() == 17


@then('a.sub_matrix(0, 2) is the following 2x2 matrix')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    assert context.a.sub_matrix(0, 2) == Matrix(2, 2, values=list(map(float, values)))


@then('a.sub_matrix(2, 1) is the following 3x3 matrix')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    assert context.a.sub_matrix(2, 1) == Matrix(3, 3, values=list(map(float, values)))


@then('b.determinant() = 25')
def step_impl(context):
    assert context.b.determinant() == 25


@then('a.minor(1, 0) = 25')
def step_impl(context):
    assert context.a.minor(1, 0) == 25


@then('a.minor(0, 0) = -12')
def step_impl(context):
    assert context.a.minor(0, 0) == -12


@then('a.cofactor(0, 0) = -12')
def step_impl(context):
    assert context.a.cofactor(0, 0) == -12


@then('a.cofactor(1, 0) = -25')
def step_impl(context):
    assert context.a.cofactor(1, 0) == -25


@then('a.cofactor(0, 0) = 56')
def step_impl(context):
    assert context.a.cofactor(0, 0) == 56


@then('a.cofactor(0, 1) = 12')
def step_impl(context):
    assert context.a.cofactor(0, 1) == 12


@then('a.cofactor(0, 2) = -46')
def step_impl(context):
    assert context.a.cofactor(0, 2) == -46


@then('a.determinant() = -196')
def step_impl(context):
    assert context.a.determinant() == -196


@then('a.cofactor(0, 0) = 690')
def step_impl(context):
    assert context.a.cofactor(0, 0) == 690


@then('a.cofactor(0, 1) = 447')
def step_impl(context):
    assert context.a.cofactor(0, 1) == 447


@then('a.cofactor(0, 2) = 210')
def step_impl(context):
    assert context.a.cofactor(0, 2) == 210


@then('a.cofactor(0, 3) = 51')
def step_impl(context):
    assert context.a.cofactor(0, 3) == 51


@then('a.determinant() = -4071')
def step_impl(context):
    assert context.a.determinant() == -4071


@then('a.determinant() = -2120')
def step_impl(context):
    assert context.a.determinant() == -2120


@then('a is invertible')
def step_impl(context):
    assert context.a.invertible()


@then('a.determinant() = 0')
def step_impl(context):
    assert context.a.determinant() == 0


@then('a is not invertible')
def step_impl(context):
    assert not context.a.invertible()


@then('a.determinant() = 532')
def step_impl(context):
    assert context.a.determinant() == 532, f'{context.a.determinant()} != 532'


@then('a.cofactor(2, 3) = -160')
def step_impl(context):
    assert context.a.cofactor(2, 3) == -160


@then('b[3,2] = -160/532')
def step_impl(context):
    assert context.b[3, 2] == 1 * Decimal(-160 / 532)


@then('a.cofactor(3, 2) = 105')
def step_impl(context):
    assert context.a.cofactor(3, 2) == 105


@then('b[2,3] = 105/532')
def step_impl(context):
    assert context.b[2, 3] == 1 * Decimal(105 / 532)


@then('b is the following 4x4 Matrix')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    assert context.b == Matrix(4, 4, values=list(map(Decimal, values)))


@then('a.inverse() is the following 4x4 Matrix')
def step_impl(context):
    values = context.table.headings + list(itertools.chain(*context.table.rows))
    assert context.a.inverse() == Matrix(4, 4, values=list(map(Decimal, values)))


@then('c * inverse(b) = a')
def step_impl(context):
    a = context.c * context.b.inverse()
    for r in range(a.row_num):
        for c in range(a.col_num):
            a[r, c] = round(a[r, c])
    assert a == context.a
