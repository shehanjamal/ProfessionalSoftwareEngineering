import time
def log_decorator(func):
    # *args and **kwargs allows any kind of input that comes to the function
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        # sstart time measurement
        start_time = time.perf_counter()
        # call the actual function
        result = func(*args, **kwargs)
        # end time measurement
        end_time = time.perf_counter()
        print(f"{func.__name__} returned {result}")
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

def use_all_mathematic_operators(a, b, c, d, e):
    addition = a + b + c + d + e
    subtraction = a - b - c - d - e
    multiplication = a * b * c * d * e
    division = a / b / c / d / e
    mixed_operations = (a + b - c) * d / e
    return {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication,
        "division": division,
        "mixed_operations": mixed_operations
    }

@log_decorator
def calculate(a, b, c, d, e):
    return use_all_mathematic_operators(a, b, c, d, e)

if __name__ == "__main__":
    result = calculate(100, 5, 2, 4, 2)
    print("Final Result:", result)