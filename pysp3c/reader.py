"""SP3c file reader."""
import os
import pathlib
from typing import Dict, List, Union


class SP3cReader:
    """SP3c file reader.

    :param Union[str, os.PathLike] file:
        input file.

    """

    def __init__(self, file: Union[str, os.PathLike]):
        self._file = pathlib.Path(file).expanduser()
        with self._file.open() as fh:
            record = ''
            data = []
            for n, text in enumerate(fh, 1):
                if n == 1:
                    self._coordinate_system = text[46:51]
                if n > 22:
                    if text.startswith('* '):
                        if record != '':
                            # process record
                            data.extend(self._parse_record(record))
                            # reset record
                            record = ''
                        record += text
                    elif text.startswith('EOF'):
                        # last line: process record
                        data.extend(self._parse_record(record))
                    else:
                        record += text
            self._data = data

    @staticmethod
    def _parse_record(record: str) -> List[Dict[str, Union[int, float, str]]]:
        lines = record.strip().split('\n')
        result = []
        # parse epoch
        year = int(lines[0][3:7])
        month = int(lines[0][8:10])
        day = int(lines[0][11:13])
        hour = int(lines[0][14:16])
        minute = int(lines[0][17:19])
        second = float(lines[0][20:31])
        for line in lines[1:]:
            obs = {
                'year': year,
                'month': month,
                'day': day,
                'hour': hour,
                'minute': minute,
                'second': second,
                'type': line[0],
                'vehicle_id': line[1:4],
                'x': float(line[4:18]),
                'y': float(line[18:32]),
                'z': float(line[32:46]),
                'clock': float(line[46:60]),
            }
            result.append(obs)
        return result

    @property
    def file(self):
        return self._file

    @property
    def data(self):
        return self._data

    @property
    def coordinate_system(self):
        return self._coordinate_system
