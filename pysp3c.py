"""SP3c file reader."""
import os
import pathlib
from typing import Union

__version__ = '0.1'


class SP3cReader:
    """SP3c file reader.

    :param Union[str, os.PathLike] file:
        input file.

    """

    def __init__(self, file: Union[str, os.PathLike]):
        self._file = pathlib.Path(file).expanduser()

    @property
    def file(self):
        return self._file
