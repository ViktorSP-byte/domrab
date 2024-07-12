from typing import Callable, Any
from functools import wraps


def log(filename: Any = None) -> Callable:
    def decorator(func: Any):
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            try:
                func(*args, **kwargs)
            except Exception as e:
                f'\n{func.__name__}: {e}. Inputs: {args}, {kwargs}'
                raise e
            else:
                output_massage = f'\n{func.__name__} ok'
                return output_massage
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f'\n{func.__name__} ok')
                else:
                    print(f'\n{func.__name__} ok')
        return inner
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

print(my_function(1, 2))
