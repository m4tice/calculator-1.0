"""main"""

from src.calculator.helper import add, sub
from src.programming_calculator.helper import hex2dec


def main():
    """
    main function
    :return: nothing
    """
    print("Result of add    :", add(1, 2))
    print("Result of sub    :", sub(1, 2))
    print("Result of hex2dec:", hex2dec("A"))


if __name__ == '__main__':
    main()
