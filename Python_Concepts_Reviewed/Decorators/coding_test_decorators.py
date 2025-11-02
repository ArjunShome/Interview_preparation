"""
Write a decorator called retry that:
	•	Takes a parameter retries (number of times to re-attempt a function if it raises an exception).
	•	Wraps any function and automatically retries execution up to n times.
	•	After all retries fail, it should raise the original exception.
	•	Prints "Retrying... (attempt X)" on each retry (except first attempt).
	•	✅ Should work on any function with any number of arguments (*args, **kwargs)
	•	✅ Must preserve function metadata (__name__, __doc__) using functools.wraps

Expected Usage -
@retry(retries=3)
def unstable_function(x):
    # randomly raise an exception for testing
    ...

unstable_function(5)

If function fails twice and succeeds on 3rd try → it should NOT raise an exception.

If it fails all 3 retries → original exception must propagate.

⸻

✅ Bonus (Optional - Senior Level)
	•	Add specific exception type filtering → only retry on certain exception types.
	•	Add delay between retries using time.sleep(seconds) without blocking main thread too long.
	•	Add exponential backoff (1s, 2s, 4s…)

"""
import functools
import time
import inspect

def retry(num_retry):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            i = 1
            last_ex = None
            while i <= num_retry:
                try:
                    print(f"Running function {func.__name__, func.__doc__, func.__annotations__, func.__dict__, inspect.signature(func).bind(*args, **kwargs)}")
                    return func(*args, **kwargs)
                except ValueError as ex:
                    last_ex = ex
                    i += 1
                    if i > num_retry:
                        raise last_ex
                    print(f"Retrying... (attempt {i})")
                    time.sleep(1)
                except ZeroDivisionError as zd:
                    raise zd
        return wrapper
    return inner



@retry(5)
def unstable_function(n):
    raise ZeroDivisionError('Humayun KHAAA!!!')

@retry(5)
def unstable_function_2(n):
    raise ValueError('Humayun KHAAA!!!')

@retry(2)
def stable_function(n):
    """
    Stable Function Docstr
    :param n:
    :return:
    """
    print(n)


if __name__=='__main__':
    try:
        stable_function(4)
        unstable_function_2(22)
        unstable_function(5)
    except Exception as v:
        print(str(v))