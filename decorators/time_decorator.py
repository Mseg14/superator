import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time() - start
        print(f'The function took: {round(finish, 6)} seconds')
        return res

    return wrapper
