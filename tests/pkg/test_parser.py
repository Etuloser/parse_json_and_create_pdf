import pytest

from pkg.barcode.parser import parse


def test_parser():
    code = "25580510000136"
    got = parse(code)
    print(got)
