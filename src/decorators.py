from typing import Callable, Any
from functools import wraps


def log(filename: Any = None) -> Callable:
    def decorator(func: Any):
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            try:
                if filename:
                    result = func(*args, **kwargs)
                    with open(filename, "a", encoding='utf-8') as file:
                        file.write('\nmy_function ok')
                else:
                    print("\nmy_function ok")

            except Exception as e:
                with open(filename, "a", encoding='utf-8') as file:
                    file.write(f'\nmy_function error: {e} Inputs: {args}, {kwargs}')
                raise Exception(f'Ошибка: {e}')
            return result
        return inner
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

print(my_function(-6, 3))
