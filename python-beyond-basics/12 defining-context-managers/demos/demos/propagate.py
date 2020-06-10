import contextlib


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception!')
        if propagate:
            raise

with propagater("outer", True), propagater("inner", False):
    raise KeyError("k")

with propagater("outer", False), propagater("inner", True):
    raise KeyError("k")