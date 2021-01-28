import pytest
from power import power
import math


def test_valid_input():
    assert power(3, 5) == math.pow(3, 5)


def test_one_base():
    assert power(1, 5) == math.pow(1, 5)


def test_zero_base():
    assert power(0, 5) == math.pow(0, 5)


def test_zero_expo():
    assert power(4, 0) == math.pow(4, 0)


def test_one_expo():
    assert power(4, 1) == math.pow(4, 1)


print(power(3, 5))
