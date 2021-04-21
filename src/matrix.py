import logging

from src.coordinates import Coordinate, convert

logger = logging.getLogger(__name__)


class MatrixError(Exception):
    pass


class Matrix(object):

    def __init__(self, row_num, col_num, values=None, default_value=0):
        self.__row_num = row_num
        self.__col_num = col_num
        if values is None:
            self.__matrix = [[default_value for _ in range(self.__col_num)] for _ in range(self.__row_num)]
        else:
            if len(values) > self.__row_num * self.__col_num:
                logger.warning(
                    f'values list exceeds size {len(values)} of Matrix size {self.__row_num * self.__col_num}. '
                    f'Skipping {values[self.__row_num * self.__col_num::]}')
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

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.__row_num == other.__row_num \
                   and self.__col_num == other.__col_num \
                   and self.__matrix == other.__matrix

    def __mul__(self, other):
        if isinstance(other, _IdentityMatrix):
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


class _IdentityMatrix(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(_IdentityMatrix, cls).__new__(cls)

        return cls._instance

    def __mul__(self, other):
        if isinstance(other, Coordinate) or isinstance(other, Matrix):
            return other
        else:
            raise MatrixError('Can only multiply by Coordinate or Matrix')

    def transpose(self):
        return self

# Singleton
IdentityMatrix = _IdentityMatrix()
