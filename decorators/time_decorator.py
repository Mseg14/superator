import time


def time_decorator(func):
    def wrapper():
        start = time.time()
        func()
        finish = time.time() - start
        print(f'The function took: {round(finish, 3)} seconds')

    return wrapper
