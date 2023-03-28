def retry(times: int, exceptions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= times:
                try:
                    return func(*args, **kwargs)
                except exceptions as error:
                    print(f'{error}, attempt %d of %d' % (attempt, times))
                    attempt += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator
