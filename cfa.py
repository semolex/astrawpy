import rawpy
import numpy as np

import echo


class CFA:
    """
    Wraps operations with CFA (Color Filter Array).
    """
    def __init__(self, raw: rawpy._rawpy.RawPy):
        self.raw = raw

    def get_pattern(self):
        """Returns Bayer/X-Trans pattern of the matrix (if possible). """
        echo.info('Getting raw CFA pattern...')
        return self.raw.raw_pattern

    def extract_cfa(self, fill=0):
        """
        Extracts color planes from the raw file.
        Pixels from other planes will be filled with passed `fill` param.

        :param fill: value that will be used to fill pixel values.
        """

        echo.info(f'Value to fill: {fill}')
        number_of_planes = self.raw.num_colors + 1
        for i in range(1, number_of_planes):
            echo.info(f'Extracting CFA plane #{i}')
            mask = (self.raw.raw_colors_visible != i)
            plane = np.copy(self.raw.raw_colors_visible)
            plane[mask] = fill
            yield i, plane

    def get_num_of_colors(self):
        return self.raw.num_colors
