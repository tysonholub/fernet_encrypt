import pathlib
import sys


def test_pythonpath():
    pysrc_path = pathlib.Path(__file__).parent.parent.joinpath("pysrc").absolute()
    assert str(pysrc_path) in sys.path
