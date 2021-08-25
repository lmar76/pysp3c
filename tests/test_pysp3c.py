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