def log_decorator(func):
    # *args and **kwargs allows any kind of input that comes to the function
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# what decorator does is takes another function as an input and allows the user to extend 
# the behavior of another function without needing to modify the current structure of the the function
@log_decorator
def add(a, b):
    return a + b

add(3, 5)
