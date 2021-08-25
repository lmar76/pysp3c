"""Test the `pysp3c` module."""
import pytest

import pysp3c


class TestSP3cReader:
    """Test the `SP3cReader` class."""

    @pytest.mark.parametrize(
        'file, exc',
        [
            ('test.sp3', None)
        ]
    )
    def test_creation(self, shared_datadir, file, exc):
        """Test instance creation."""
        if exc:
            with pytest.raises(exc):
                _ = pysp3c.SP3cReader(shared_datadir / file)
        else:
            assert isinstance(
                pysp3c.SP3cReader(shared_datadir / file),
                pysp3c.SP3cReader
            )

    @pytest.mark.parametrize(
        'file, expected',
        [
            (
                'test.sp3',
                [
                    {
                        'year': 2021,
                        'month': 8,
                        'day': 11,
                        'hour': 0,
                        'minute': 0,
                        'second': 18.0,
                        'type': 'P',
                        'vehicle_id': 'L47',
                        'x': 6461.886846,
                        'y': 2100.852059,
                        'z': -473.263449,
                        'clock': 0.007519,
                    }
                ]
            )
        ]
    )
    def test_data(self, shared_datadir, file, expected):
        """Test the `SP3cReader.data` property."""
        sp3 = pysp3c.SP3cReader(shared_datadir / file)
        assert len(sp3.data) == 8
        assert sp3.data[0] == expected[0]
