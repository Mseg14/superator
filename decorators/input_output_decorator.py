from decorators.data_mask import MaskingManager


def function_details(func):
    masking_manager = MaskingManager()
    arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
    func_name = func.__name__

    def wrapper(*args, **kwargs):
        arg_values = ', '.join([f'{i[0]} = {masking_manager.mask(i[1])}' for i in zip(arg_names, args[:len(arg_names)])])
        print(f'{func_name} was called with the params: {arg_values}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func_name}, returned the value: {masking_manager.mask(result)}')

    return wrapper
