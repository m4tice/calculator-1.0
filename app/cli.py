"""
author: @guu8hc
"""
#pylint: disable=line-too-long

import argparse
from app.calculator import Calculator

def main():
    """
    main cli function
    """
    parser = argparse.ArgumentParser(description="Calculator CLI")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide", "power", "factorial", "is_prime", "root"], help="Operation to perform")
    parser.add_argument("operands", nargs="+", type=float, help="Operands for the operation")

    args = parser.parse_args()
    print(f"DEBUG: {args}")
    calc = Calculator()
    result = None

    if args.operation == "add":
        result = calc.add(*args.operands)
    elif args.operation == "subtract":
        result = calc.subtract(*args.operands)
    elif args.operation == "multiply":
        result = calc.multiply(*args.operands)
    elif args.operation == "divide":
        result = calc.divide(*args.operands)
    elif args.operation == "power":
        result = calc.power(*args.operands)
    elif args.operation == "factorial":
        result = calc.factorial(int(args.operands[0]))
    elif args.operation == "is_prime":
        result = calc.is_prime(int(args.operands[0]))
    elif args.operation == "root":
        result = calc.root(*args.operands)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
