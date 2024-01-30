import logging
import math
from decimal import Decimal, getcontext

from src import EPSILON

logger = logging.getLogger(__name__)


class MatrixError(Exception):
    pass


class RotationMatrixError(Exception):
    pass


class ScalarNotPoint(Exception):
    pass


class ScalarNotVector(Exception):
    pass


class Matrix:

    def __init__(self, row_num, col_num, values=None, default_value=Decimal(0)):
        self.__row_num = row_num
        self.__col_num = col_num
        if values is None:
            self.__matrix = [[default_value for _ in range(self.__col_num)] for _ in range(self.__row_num)]
        else:
            if len(values) > self.__row_num * self.__col_num:
                logger.warning(
                    f'values list size {len(values)} exceeds size of Matrix {self.__row_num * self.__col_num}. '
                    f'Skipping {values[self.__row_num * self.__col_num::]}')
            elif len(values) < self.__row_num * self.__col_num:
                values += [Decimal(default_value) for _ in range(self.__row_num * self.__col_num - len(values))]
            values = list(map(getcontext().create_decimal, values))
            self.__matrix = [values[i:i + self.__col_num] for i in range(0, len(values), self.__col_num)][
                            :self.__row_num]

    @property
    def row_num(self):
        return self.__row_num

    @property
    def col_num(self):
        return self.__col_num

    def __getitem__(self, indices):
        row, col = indices
        return self.__matrix[row][col]

    def __setitem__(self, indices, value):
        row, col = indices
        self.__matrix[row][col] = Decimal(value)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        if self.__row_num != other.__row_num or self.__col_num != other.__col_num:
            return False

        return all(not all(self[row, col] - other[row, col] > EPSILON for col in range(self.__col_num)) for row in
                   range(self.__row_num))
        # for row in range(self.__row_num):
        #     for col in range(self.__col_num):
        #         if self[row, col] - other[row, col] > EPSILON:
        #             return False
        #
        # return True

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise MatrixError('Can only multiply by Scalar or Matrix')

        elif isinstance(other, IdentityMatrix):
            return self

        else:
            if self.col_num != other.row_num:
                raise MatrixError('Right Matrix\'s column number must equal left Matrix\'s row number')

            values = []

            for m in range(self.row_num):
                for p in range(other.col_num):
                    v = 0
                    for n in range(self.col_num):
                        v += self[m, n] * other[n, p]
                    values.append(v)

            if isinstance(other, Scalar):
                return convert(Scalar(*values))

            return Matrix(self.row_num, other.col_num, values)

    def transpose(self):
        values = []
        for c in range(self.col_num):
            for r in range(self.row_num):
                values.append(self[r, c])

        return Matrix(self.col_num, self.row_num, values=values)

    def determinant(self):
        if self.row_num == self.col_num == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]
        determinant = 0
        for col in range(self.col_num):
            determinant += self[0, col] * self.cofactor(0, col)
        return determinant

    def sub_matrix(self, row, column):
        values = []
        for row_index, r in enumerate(self.__matrix):
            if row_index != row:
                values += r[:column] + r[column + 1:]
        return Matrix(self.row_num - 1, self.col_num - 1, values=values)

    def minor(self, row, column):
        return self.sub_matrix(row, column).determinant()

    def cofactor(self, row, column):
        minor = self.minor(row, column)
        if ((row + column) % 2) != 0:
            minor = -minor
        return minor

    def invertible(self):
        return self.determinant() != 0

    def inverse(self):
        if not self.invertible():
            raise MatrixError('Matrix is not invertible')
        determinant = self.determinant()
        inverse_matrix = Matrix(self.row_num, self.col_num)
        for row in range(self.row_num):
            for col in range(self.col_num):
                cofactor = self.cofactor(row, col)
                inverse_matrix[col, row] = cofactor / determinant

        return inverse_matrix

    # Transformations
    def translate(self, x, y, z):
        return TranslationMatrix(x, y, z) * self

    def scale(self, x, y, z):
        return ScalingMatrix(x, y, z) * self

    def rotate(self, x_radians=None, y_radians=None, z_radians=None):
        return RotationMatrix(x_radians=x_radians, y_radians=y_radians, z_radians=z_radians) * self

    def shear(self, x_y=0, x_z=0, y_x=0, y_z=0, z_x=0, z_y=0):
        return ShearingMatrix(x_y=x_y, x_z=x_z, y_x=y_x, y_z=y_z, z_x=z_x, z_y=z_y) * self


class Scalar(Matrix):

    def __init__(self, x, y, z, w):
        super(Scalar, self).__init__(4, 1, [x, y, z, w])

    @property
    def x(self):
        return self[0, 0]

    @property
    def y(self):
        return self[1, 0]

    @property
    def z(self):
        return self[2, 0]

    @property
    def w(self):
        return self[3, 0]

    def is_a_point(self):
        return self.w == Point.w

    def is_a_vector(self):
        return self.w == Vector.w

    def __to_point(self):
        if self.is_a_point():
            return Point(self.x, self.y, self.z)
        raise ScalarNotPoint()

    def __to_vector(self):
        if self.is_a_point():
            return Vector(self.x, self.y, self.z)
        raise ScalarNotVector()

    def __convert(self):
        if self.is_a_point():
            return Point(self.x, self.y, self.z)
        elif self.is_a_vector():
            return Vector(self.x, self.y, self.z)
        return self

    def __eq__(self, other):
        if isinstance(other, Scalar):
            return self.x.quantize(5) == other.x.quantize(5) and \
                self.y.quantize(5) == other.y.quantize(5) and \
                self.z.quantize(5) == other.z.quantize(5) and \
                self.w.quantize(5) == other.w.quantize(5)
        return NotImplemented

    # TODO: Not sure what happens when adding a point to a point
    def __add__(self, other):
        return Scalar(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w
        ).__convert()

    # TODO: Only works for 2 point to get a vector
    def __sub__(self, other):
        return Scalar(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w
        ).__convert()

    def __neg__(self):
        return (Scalar(0, 0, 0, 0) - self).__convert()

    def __mul__(self, other):
        scalar = Decimal(other)
        return Scalar(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
            self.w * scalar
        ).__convert()

    def __truediv__(self, other):
        scalar = Decimal(other)
        return Scalar(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar,
            self.w / scalar
        ).__convert()


class Point(Scalar):
    w: Decimal = Decimal(1)

    def __init__(self, x, y, z):
        super(Point, self).__init__(x, y, z, self.w)


def point():
    return Point(0, 0, 0)


class Vector(Scalar):
    w: Decimal = Decimal(0)

    def __init__(self, x, y, z):
        super(Vector, self).__init__(x, y, z, self.w)

    def magnitude(self):
        return Decimal(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))

    def normalize(self):
        magnitude = self.magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude
        )

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def reflect(self, normal):
        return self - normal * 2 * self.dot(normal)


def convert(coordinate: Scalar):
    if coordinate.is_a_point():
        return Point(coordinate.x, coordinate.y, coordinate.z)
    elif coordinate.is_a_vector():
        return Vector(coordinate.x, coordinate.y, coordinate.z)
    return coordinate


class IdentityMatrix(Matrix):
    _instance = None

    def __init__(self, size=4):
        super(IdentityMatrix, self).__init__(size, size)
        for i in range(size):
            self[i, i] = 1

    def __mul__(self, other):
        if not isinstance(other, (Scalar, Matrix)):
            raise MatrixError('Can only multiply by Scalar or Matrix')

        return other

    def transpose(self):
        return self


def identity_matrix():
    return IdentityMatrix()


class TranslationMatrix(Matrix):

    def __init__(self, x, y, z):
        values = [
            1, 0, 0, x,
            0, 1, 0, y,
            0, 0, 1, z,
            0, 0, 0, 1
        ]
        super(TranslationMatrix, self).__init__(4, 4, values=values)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return other
        else:
            return super(TranslationMatrix, self).__mul__(other)


class ScalingMatrix(Matrix):

    def __init__(self, x, y, z):
        values = [
            x, 0, 0, 0,
            0, y, 0, 0,
            0, 0, z, 0,
            0, 0, 0, 1
        ]
        super(ScalingMatrix, self).__init__(4, 4, values=values)


class RotationMatrix(Matrix):

    def __init__(self, x_radians=None, y_radians=None, z_radians=None):
        args = [i for i in [x_radians, y_radians, z_radians] if i is not None]
        if len(args) != 1:
            raise RotationMatrixError('Exactly one radians kwarg is required.')
        values = None
        if x_radians:
            values = [
                1, 0, 0, 0,
                0, math.cos(x_radians), -math.sin(x_radians), 0,
                0, math.sin(x_radians), math.cos(x_radians), 0,
                0, 0, 0, 1
            ]
        elif y_radians:
            values = [
                math.cos(y_radians), 0, math.sin(y_radians), 0,
                0, 1, 0, 0,
                -math.sin(y_radians), 0, math.cos(y_radians), 0,
                0, 0, 0, 1
            ]
        elif z_radians:
            values = [
                math.cos(z_radians), -math.sin(z_radians), 0, 0,
                math.sin(z_radians), math.cos(z_radians), 0, 0,
                0, 0, 1, 0,
                0, 0, 0, 1
            ]

        super(RotationMatrix, self).__init__(4, 4, values=values)


class ShearingMatrix(Matrix):

    def __init__(self, x_y=0, x_z=0, y_x=0, y_z=0, z_x=0, z_y=0):
        values = [
            1, x_y, x_z, 0,
            y_x, 1, y_z, 0,
            z_x, z_y, 1, 0,
            0, 0, 0, 1
        ]
        super(ShearingMatrix, self).__init__(4, 4, values=values)
