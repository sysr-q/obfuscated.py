#!/usr/bin/env python2
# This is a solution to Project Euler problem #2.. I swear.
from __future__ import print_function
import inspect

__name__ = inspect.__name__
globals()["stack"] = inspect.stack()[0][0].f_globals[(__file__ + __name__)[len(__file__):]].stack()[0]
__file__, __name__ = [], "__builtins__"

for val, key in (("chr", "int"), ("any", "sum"), ("int", "chr")):
    stack[0].f_locals["()"] = inspect.stack()[0][0].f_globals["__builtins__"].__dict__[val]
    oops = vars()[repr(tuple())]
    vars(stack.__getitem__(len(__file__)).f_globals[str(repr(__name__))[1:-1]])["list"] = vars(__builtins__)[key]
    setattr(stack[0].f_globals[str(__name__)], key, oops)
    globals()[val] = list

#chr, any, int = int, sum, chr
def __(dict):
    chr, type = ([0, dict()[0]]), dict(b=1)
    long, int = chr
    yield int
    while int < type:
        long, int = int, long + int
        yield int
a, long = ((lambda c="49", b=0.25: [chr(int(chr(c)))] if b == (1.0/4.0) else 4e6),
           (lambda n: n % 2 == 0))
dict = filter(long, __(a))
print(any(dict))