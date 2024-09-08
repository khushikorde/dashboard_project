import logging
import sys

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception(f"Error: {e}")
            return sys.exc_info()

    return wrapper

# Example usage
@handle_exceptions
def divide(a, b):
    return a / b

# Set up logging
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

# Call the function
try:
    result = divide(10, 0)
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")