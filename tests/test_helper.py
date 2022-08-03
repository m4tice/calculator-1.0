"""Test helper"""

from src.calculator.helper import add


def test_add():
    """
    Test add function
    :return:
    """
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
