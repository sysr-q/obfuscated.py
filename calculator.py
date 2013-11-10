#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
a = lambda s: __import__(s)
b = a("operator")
c = {"+": b.add, "-": b.sub, "/": b.div, "*": b.mul}
d = type("rot13", (), {"__doc__": "x\x9cs\xcbHNNJM/*THJ.J\xcdKOJM\xb3\x02\x00N\xe6\x07~".decode("zlib")})
e = print(d.__doc__.decode(d.__name__), " ".join(c.keys()))
while e not in c:
    e = raw_input("OP: ")
e = c[e]
c = lambda d="> ": float(raw_input(d))
f, g = (c(), c())
b = print(e(f, g))
