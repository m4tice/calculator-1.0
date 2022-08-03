"""Test helper"""

from src.calculator.helper import add, sub


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
