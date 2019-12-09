# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-10-18 12:28:22
# @Last Modified by:   razor87
# @Last Modified time: 2019-12-05 19:21:06


def my_decorator(f):
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')


def first_decorator(func):
    def wrapped():
        print('Inside first_decorator product')
        return func()
    return wrapped


def second_decorator(func):
    def wrapped():
        print('Inside second_decorator product')
        return func()
    return wrapped

@first_decorator
@second_decorator
def decorated():
    print('Finally called...')

# decorated = first_decorator(second_decorator(decorated))
decorated()



def bool_or_nothing(func):
    def wrapper(arg):
        # if arg in {0, 1}:
        #     return func(arg)
        # return None
        return (func(arg)
                if isinstance(arg, bool)
                else None)
    return wrapper

@bool_or_nothing
def foo(arg):
    return not arg


def get_multiplier(number):
    def inner(a):
        return a * number
    return inner


def logger(func):    # decorator
    @functools.wraps(func)    # import functools
    def wrapped(*args, **kwargs):
        result = func(num_list)
        result *= 2
        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)
print('Summator: {}'.format(summator(list(range(6)))))





def frames(f):
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwds):
        from inspect import currentframe
        frame = currentframe()
        print('current value:', args)
        print('current frame:', frame)
        print('parent  frame:', frame.f_back)
        print('code object', frame.f_code)
        return f(*args, **kwds)
    return wrapper



def memoize(func):
    """simplest memoizing decorator"""
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized





def clock(func):
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


def clock_(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked


def memoize(fn, slot=None, maxsize=32):
    """Memoize fn: make it remember the computed value for any argument list.
    If slot is specified, store result in that slot of first argument.
    If slot is false, use lru_cache for caching the values."""
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        @functools.lru_cache(maxsize=maxsize)
        def memoized_fn(*args):
            return fn(*args)

    return memoized_fn





def memoize_uw(func):
    func.cache = {}


def memoize(*args, **kw):
    if kw:  # frozenset is used to ensure hashability
        key = args, frozenset(kw.items())
    else:
        key = args

    if key not in func.cache:
        func.cache[key] = func(*args, **kw)
        return func.cache[key]
    return functools.update_wrapper(memoize, func)


def _memoize(func, *args, **kw):
    if kw:  # frozenset is used to ensure hashability
        key = args, frozenset(kw.items())
    else:
        key = args

    cache = func.cache  # attribute added by memoize
    if key not in cache:
        cache[key] = func(*args, **kw)
    return cache[key]


def memoize(f):
    """
    A simple memoize implementation. It works by adding a .cache dictionary
    to the decorated function. The cache will grow indefinitely, so it is
    your responsibility to clear it, if needed.
    """
    from decorator import decorate
    f.cache = {}
    return decorate(f, _memoize)




def fib1(n):
    sys.setrecursionlimit(100000)
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

fib1 = lru_cache(maxsize=None)(fib1)


@functools.lru_cache(maxsize=None)
def fib(n):
    # from literateprograms.org
    # http://bit.ly/hlOQ5m
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

