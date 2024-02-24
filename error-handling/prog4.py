class CustomError(Exception):
    pass

def divide_numbers(a, b):
    if b == 0:
        raise CustomError("Division by zero is not allowed.")
    return a / b

def main():
    try:
        result = divide_numbers(10, 0)
        print(f"Result: {result}")
    except CustomError as e:
        print(f"Error: {e}")

main()