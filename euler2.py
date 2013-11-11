#!/usr/bin/env python2
# This is a solution to Project Euler problem #2.. I swear.
from __future__ import print_function
import inspect

__name__ = inspect.__name__
globals()["stack"] = inspect.stack()[0][0].f_globals[(__file__ + __name__)[len(__file__):]].stack()[0]
locals()["panic"] = lambda: len(__file__[-1])-1
globals()["carrying_a_towel"] = lambda square: square % 2 == 0
__file__, __name__ = [(("chr", "int"), ("any", "sum"), ("int", "chr"), ("foo", lambda: []))], "__builtins__"

for dont, look in enumerate(__file__[0]):
    val, key = look
    if dont == panic():
        globals().update({val: look[-1]})
        continue
    stack[0].f_locals["()"] = inspect.stack()[0][0].f_globals["__builtins__"].__dict__[val]
    oops = vars()[repr(tuple())]
    vars(stack.__getitem__(len(__file__) - len(__file__)).f_globals[str(repr(__name__))[1:-1]])["list"] = vars(__builtins__)[key]
    setattr(stack[0].f_globals[str(__name__)], key, oops)
    globals()[val] = list

def hitch():
    dont, panic = [0, 1], 4e6
    always, carry = dont
    a_towel = lambda yes, no="carry":yes[no]
    yield carry
    while carry < panic:
        always, carry = carry, always + carry
        yield a_towel(locals())

print(any(filter(carrying_a_towel, hitch())))
