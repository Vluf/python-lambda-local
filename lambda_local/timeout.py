'''
Copyright 2015-2017 HDE, Inc.
Licensed under MIT.
'''

from threading import Timer
from contextlib import contextmanager


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    def timeout_handler():
        raise TimeoutException("Timeout after {} seconds.".format(seconds))
    t = Timer(seconds, timeout_handler)
    t.start()
    try:
        yield
    finally:
        signal.alarm(0)
