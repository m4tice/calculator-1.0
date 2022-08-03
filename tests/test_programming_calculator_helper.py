"""Test programming calculator helper"""

from src.programming_calculator.helper import hex2dec


def test_hex2dec():
    """
    Test hex2dec function
    :return:
    """
    assert hex2dec("A") == 10
    assert hex2dec("0F") == 15
    assert hex2dec("AA") == 170
