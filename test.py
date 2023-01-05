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


if __name__ == '__main__':
    @calcutimeit
    def tt():
        import time
        time.sleep(1)


    tt()
    print('ok.')

