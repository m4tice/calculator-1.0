"""Test helper"""

from src.calculator.helper import add, sub, mul


def test_add():
    """
    Test add function
    :return:
    """
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    assert add(-1, 2) == 1


def test_sub():
    """
    Test sub function
    :return:
    """
    assert sub(1, 2) == -1
    assert sub(-1, -2) == 1
    assert sub(-1, 2) == -3


def test_mul():
    """
    Test mul function
    :return:
    """
    assert mul(1, 2) == -1
    assert mul(-1, -2) == 1
    assert mul(-1, 2) == -3
