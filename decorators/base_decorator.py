def base_decorator(func):
    def wrapper():
        print('I am called before the function invocation!')
        func()
        print('It seems the function invocation is done')

    return wrapper
