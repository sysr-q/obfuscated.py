#!/usr/bin/env python2
eggs = "spam"

x = r'''
def derp():
	try:
		print "eggs =", eggs
	except NameError:
		print "[no eggs]"
	try:
		global eggs
		print "eggs =", eggs
	except NameError:
		print "[no global eggs]"
	try:
		import inspect
		print "eggs =", inspect.stack()[-1][0].f_globals["eggs"]
	except NameError:
		print "[no inspected eggs]"
derp()
'''

d = {}
exec x in d
"""
± python2 exec_escape.py
<string>:8: SyntaxWarning: name 'eggs' is used prior to global declaration
eggs = [no eggs]
eggs = [no global eggs]
eggs = spam
"""
