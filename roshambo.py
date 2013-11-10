#!/usr/bin/env python2
# -*- coding: utf-8 -*-
h = type("", (), {})
a = "__gt__"
c = type("Scissors", (h,), {a: lambda a,c: o(c,k)})
k = type("Paper", (h,), {a: lambda c,k: o(k,f)})
f = type("Rock", (h,), {a: lambda h,a: o(a,c)})
o = isinstance
r = {c.__name__.lower():c for c in h.__subclasses__()}
u = None
m = lambda r: __import__(r)
s = m("random").choice(h.__subclasses__())()
while u not in r:
    u = raw_input("[scissors/paper/rock]: ").lower()
n = (r[u]())
e = "You {0}!\n".format("tie" if n.__class__ == s.__class__ else ("win" if n > s else "lose"))
t = m("sys").stdout.write(e)
