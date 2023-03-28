import random
import time
import hashlib

from typing import List

from decorators.base_decorator import base_decorator
from decorators.input_output_decorator import function_details
from decorators.retry_decorator import retry
from decorators.time_decorator import time_decorator


@base_decorator
def say_whee():
    print("Whee!!!")


@time_decorator
def count_to_random_number():
    random_number = random.randint(1, 5)
    for i in range(random_number):
        time.sleep(i)


@function_details
def how_many_words(words: List[str]):
    return len(words)


@retry(times=3, exceptions=(ValueError, AssertionError))
def just_raise_errors():
    print("I WAS CALLED!")
    raise BlockingIOError("This is on purpose")


@time_decorator
@function_details
def returns_secret_information(aws_key: str, aws_account_name: str):
    super_secret_string = aws_key + aws_account_name
    return hashlib.sha256(bytes(super_secret_string, encoding='utf8')).hexdigest()[:8]


if __name__ == '__main__':
    returns_secret_information("137264121843", "michael@aws.org")
