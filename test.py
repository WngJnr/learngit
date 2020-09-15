# -*- coding: utf-8 -*-

import functools
from timeit import default_timer as timer

def calcutimeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        _start = timer()
        _ret = func(*args, **kw)
        _end = timer()
        print('%s() executed: %.3f seconds' % (func.__name__, _end - _start))
        return _ret

    return wrapper
