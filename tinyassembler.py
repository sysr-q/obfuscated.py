#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# This was written for an r/dailyprogrammer challenge:
# http://www.reddit.com/r/dailyprogrammer/comments/1kqxz9/080813_challenge_132_intermediate_tiny_assembler/
# There's an input file at the bottom in a string.
___________________ = filter
________________________ = len
from re import compile as ________________
____________________ = type(len(""))
from string import digits as __________________
_____________________ = map
_ = lambda b, a: a.upper().strip().split()
b = type("", (), {"__doc__": "Vainyvq Nethzragf, {0} <vachg_svyranzr>", "__call__": _})
__ = type("__", (b,), {"__call__": lambda c, a, *b: "".join(p[c] for c in (a,) + b)})
___________________________ = enumerate
n = __name__
______________________ = None
import sys
i = lambda s: sys.stdout.write(s + "\n")
____________________________ = range
_____________________________ = exit
_______________________ = hex
from string import ascii_uppercase as p


def parse(___________):
    """x_\x9cq\x0b_\xc9f\xcc3\xab~td,:.=NN\xcdIMT\xcaKI!-j\xd2:QI\xc8Z,ZJ!\xd6iKu\xc9,\xcfHK6OZ\xce*/f*9\xd0#\xcbu/IJ6\x07]\x00C\xbc{\xd7t\x0ba\xcdU
    Once upon a midnight dreary, while I pondered weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, [__znva__] suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    `'Tis some visitor,' I muttered, `tapping at my chamber door -
    Only this, and nothing more.'
    """

    _______=________________('^([a-zA-Z]+)' + '?))q\\|]\\q\\[\\(+f\\:?('.decode("rot13")[::-1]*3 + '$').match

    def __________(_________________________, __________________________):
        raise Exception("Exception {0} at line {1}".format(_________________________, __________________________))
        _____________________________()

    ___ = {
        __()(0,13,3): {'11': 0, '10': 1},
        __()(9,11,18): {'010': 27, '0' + str(ord(p[0])-54): 25, str(85+len(p)): 24, '110': 26},
        __()(9,4,16): {'010': 23, '011': 21, '111': 20, '110': 22},
        __()(23,14,17): {'11': 4, '10': 5},
        __()(18,20,1): {'11': 12, '10': 13},
        __()(9,25): {'11': 16, '10': 17, '00': 19, '01': 18},
        __()(9,12,15): {'1': 14, '0': 15},
        __()(17,0,13,3,14,12): {'1': 9},
        __()(12,14,21): {'11': 7, '10': 8},
        __()(3,15,17,8,13,19): {'1': 34, '0': 35},
        __()(0,15,17,8,13,19): {'1': 32, '0': 33},
        __()(0,3,3): {'11': 10, '10': 11},
        __()(13,14,19): {'1': 6},
        __()(9,6,19): {'010': 31, '011': 29, '111': 28, '110': 30},
        __()(14,17): {'11': 2, '10': 3},
        __()(7,0,11,19): {None: 255}
    }

    for ________, _________ in ___________________________(___________):
        if _______(_________) is ______________________:
            __________(1, ________)
        _________ = b()(_________)
        if _________[0] not in ___:
            __________(2, ________) 
        _____________ = "".join(_____________________(lambda ____________: str(____________________('[' in ____________)), _________[1:]))
        if not _____________:
            _____________ = ______________________
        if _____________ not in ___[_________[0]]:
            __________(3, ________)
        _______________=(_______________________(___[_________[0]][_____________]), _____________________(lambda _________________: _______________________(____________________(___________________(lambda ________________: ________________ in __________________, _________________))), (_________[1:])))
        i((_______________[0]+" "+" ".join([______________ for ______________ in _______________[1]])).strip())

if n == parse.__doc__[243:251].decode("rot13"):
    i(parse.__doc__[:78:2].decode("zlib"))

    if len(sys.argv) != 2:
        i(b.__doc__.decode("rot13").format(__file__))
        exit()

    with open(sys.argv[1], "r") as input_file:
        parse(input_file.read().strip().split("\n"))

# input.txt:
"""
Mov [2] 0
Mov [3] 0
Jeq 6 [3] [1]
Add [3] 1
Add [2] [0]
Jmp 2
Mov [0] [2]
Halt
"""
