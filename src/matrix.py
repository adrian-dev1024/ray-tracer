import logging

logger = logging.getLogger(__name__)


class Matrix:

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

    def __getitem__(self, indices):
        row, col = indices
        return self.__matrix[row][col]

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.__row_num == other.__row_num \
                   and self.__col_num == other.__col_num \
                   and self.__matrix == other.__matrix
