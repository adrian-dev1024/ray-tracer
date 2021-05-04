import logging
from decimal import Decimal, getcontext

from src.coordinates import Coordinate, convert

logger = logging.getLogger(__name__)


class MatrixError(Exception):
    pass


class Matrix(object):

    def __init__(self, row_num, col_num, values=None, default_value=Decimal(0)):
        self.__row_num = row_num
        self.__col_num = col_num
        if values is None:
            self.__matrix = [[default_value for _ in range(self.__col_num)] for _ in range(self.__row_num)]
        else:

            if len(values) > self.__row_num * self.__col_num:
                logger.warning(
                    f'values list exceeds size {len(values)} of Matrix size {self.__row_num * self.__col_num}. '
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
        if isinstance(other, Matrix):
            return self.__row_num == other.__row_num \
                   and self.__col_num == other.__col_num \
                   and self.__matrix == other.__matrix
        return False

    def __mul__(self, other):
        if isinstance(other, IdentityMatrix):
            return self
        if isinstance(other, Coordinate):
            res = self * Matrix(4, 1, [other.x, other.y, other.z, other.x])
            return convert(Coordinate(res[0, 0], res[1, 0], res[2, 0], res[3, 0]))
        elif isinstance(other, Matrix):
            if self.col_num != other.row_num:
                raise MatrixError('Right Matrix\'s column number must equal left Matrix\'s row number')
            values = []
            for m in range(self.row_num):
                for p in range(other.col_num):
                    v = 0
                    for n in range(self.col_num):
                        v += self[m, n] * other[n, p]
                    values.append(v)
            return Matrix(self.row_num, other.col_num, values)
        else:
            raise MatrixError('Can only multiply by Coordinate or Matrix')

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


class IdentityMatrix(Matrix):
    _instance = None

    def __init__(self, size):
        super(IdentityMatrix, self).__init__(size, size)
        for i in range(size):
            self[i, i] = 1

    def __mul__(self, other):
        if isinstance(other, Coordinate) or isinstance(other, Matrix):
            return other
        else:
            raise MatrixError('Can only multiply by Coordinate or Matrix')

    def transpose(self):
        return self
