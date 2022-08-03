"""main"""

from src.calculator.helper import add, sub
from src.programming_calculator.helper import hex2dec


def main():
    """
    main function
    :return: nothing
    """
    print(add(1, 2))
    print(sub(1, 2))
    print(hex2dec("A"))


if __name__ == '__main__':
    main()
