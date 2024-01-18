import pytest

from pkg.barcode.parser import parse
from pkg.barcode.encoder import encode


def test_encode():
    id = "25580510000136"
    path = parse(id)
    got = encode(path)
    print(got)
