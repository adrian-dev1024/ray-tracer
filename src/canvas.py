from src.color import Color


class Canvas:

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._grid = [[Color(0, 0, 0) for _ in range(self.width)] for _ in range(self.height)]

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def grid(self):
        return self._grid

    def write_pixel(self, x: int, y: int, color: Color):
        self.grid[x][y] = color

    def pixel_at(self, x: int, y: int):
        return self.grid[x][y]

    def __str__(self):
        string = ''
        for inner in self._grid:
            for color in inner:
                string += f'| {str(color)} '
            string += '|\n'
        return string
