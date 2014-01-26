#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
eggs = "spam"


y = '''(lambda inspect, n: (lambda us, stack: print(stack[stack.index(us)+2][0].f_globals[n]))([s for s	in inspect.stack() if s[3] == "<lambda>"][0], inspect.stack()))(__import__("inspect"), "eggs")'''

d = {}
exec y in d
"""
spam
"""

print("-"*50)

x = r'''
def derp():
	try:
		print("eggs =", eggs)
	except NameError:
		print("[no eggs]")
	try:
		global eggs
		print("eggs =", eggs)
	except NameError:
		print("[no global eggs]")
	try:
		import inspect
		stack = inspect.stack()
		us = [s for s in stack if s[3] == "derp"][0]
		them = stack[stack.index(us)+2]
		print("eggs =", them[0].f_globals["eggs"])
	except NameError:
		print("[no inspected eggs]")
derp()
'''

d = {}
exec x in d
"""
<string>:8: SyntaxWarning: name 'eggs' is used prior to global declaration
eggs = [no eggs]
eggs = [no global eggs]
eggs = spam
"""
