## Python 2:
# Easy:
imp = [v for k, v in [x for x in ().__class__.__base__.__subclasses__() if x.__name__ == "catch_warnings"][0]()._module.__builtins__.items() if "imp" in k][0]
# Hardmode: no double underscores
imp = (lambda n: [v for k, v in getattr([x for x in getattr(getattr(getattr((), n+"class"+n), n+"base"+n), n+"subclasses"+n)() if getattr(x, n+"name"+n) == "catch_warnings"][0]()._module, n+"builtins"+n).items() if "imp" in k][0])("_"*2)
