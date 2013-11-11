#!/usr/bin/env python2
# The fun bits of obfuscating Python.

# Fuck with the top stack:
import inspect
def _get_namespace(globals=True):
    pprint.pprint(inspect.stack())
    namespace = getattr(inspect.stack()[-1][0], "f_globals" if globals else "f_locals")
    return namespace

def set(ident, var):
    namespace = _get_namespace()
    namespace[ident] = var

def get(ident):
    namespace = _get_namespace()
    return namespace[ident]
