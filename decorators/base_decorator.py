def base_decorator(func):
    def wrapper(*args, **kwargs):
        print('I am called before the function invocation!')
        func(*args, **kwargs)
        print('It seems the function invocation is done')

    return wrapper
