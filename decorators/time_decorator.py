import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        finish = time.time() - start
        print(f'The function took: {round(finish, 6)} seconds')

    return wrapper
