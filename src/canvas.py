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
        self.grid[y][x] = color

    def pixel_at(self, x: int, y: int):
        return self.grid[y][x]

    def to_ppm(self):
        ppm_string = f'P3\n{self._width} {self.height}\n255\n'
        for inner in self.grid:
            line = ''
            for pixel in inner:
                for color in [pixel.red, pixel.green, pixel.blue]:
                    if color < 0:
                        value = '0 '
                    elif color > 1:
                        value = '255 '
                    else:
                        value = f'{round(255 * color)} '
                    # Splitting lines over 70 characters long
                    if len(line) + len(value) > 70:
                        ppm_string += f'{line[:-1]}\n'
                        line = ''
                    line += value

            ppm_string += f'{line[:-1]}\n'

        return ppm_string

    def __str__(self):
        string = ''
        for inner in self._grid:
            for color in inner:
                string += f'| {str(color)} '
            string += '|\n'
        return string
