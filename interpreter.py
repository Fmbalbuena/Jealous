import sys
code_page = "|¬°!1\"2#3$4%5&6/7(8)9=0?'\\¿¡\tq@wertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM¨´+*~{}^`[],.-_:;<>éýúíóáÉÝÚÍÓÁèùìòàÈÙÌÒÀêûî"
code_page += "ôâÊÛÎÔÂ\nëÿüöïäËÜÖÏÄᐍᐎᐓᐗᎾᚁᚂᚃᚄᚅᚆᚇᚈᚉᚊᚋᚌᚍᚎᚏᏔᏕᏖᏗᏘᏙᏚᏛᏜᏝᏞᏟᏠᏡᏢᏣᏤᏥᏦᏧᏨᏩᏪᏫᏬᏭᏮᏯᏰᏱᏲᏳᏴᏵᏸᏹᏺᏻᏼᏽᎳᎴᎵᎶᎷᎸᎹᎺᎻᎼᎽᎿᏀᏁᏂᏃᏄᏅᏆᏇᏈᏉᏊᏋᏌᏍᏎᏏᏐᏑᏒᏓ×ĀāĂăĄąĆćĈĉĊċČčĎaĐ"
i=""
from sympy.ntheory.primetest import isprime as prime_check
with open(sys.argv[1], 'rb') as file:
    code = file.read()
    code = "".join(code_page[i] for i in code)
# Golfing language interpreter
lines = code.split("\n")
arguments = sys.argv[2:]
dyadiccommands = {
    "×": lambda x, y: x * y,
    "Ꮎ": lambda x, y: x / y,
    "|": lambda x, y: x + y,
    "¬": lambda x, y: x - y,
    "°": lambda x, y: x % y,
    "#": lambda x, y: x ** y,
    "\\": lambda x, y: x // y,
    "\t": lambda x, y: x ** (1 / y),
}
from math import factorial
import math
monadiccommands = {
    "!": lambda x: factorial(x),
    "A": lambda x: x.capitalize(),
    "B": lambda x: x.swapcase(),
    "C": lambda x: x.lower(),
    "D": lambda x: x.upper(),
    "E": lambda x: int(x),
    "F": lambda x: float(x),
    "G": lambda x: [x] * x if type(x) == int else [x] * len(x),
    "H": lambda x: x / 2,
    "I": lambda x: x + 1,
    "J": lambda x: 1j * x,
    "K": lambda x: 2 * x,
    "L": lambda x: len(x),
    "M": lambda x: math.ceil(x),
    "N": lambda x: -x,
    "Ñ": lambda x: math.floor(x),
    "O": lambda x: x ** 2,
    "P": lambda x: x[0] + x[-1],
    "Q": lambda x: x[0],
    "R": lambda x: x[::-1],
    "S": lambda x: x[1:],
    "T": lambda x: x[:-1],
    "U": lambda x: x * x * x,
    "V": lambda x: [x for x in range(x)],
    "W": lambda x: [x for x in range(1, x)],
    "X": lambda x: [x for x in range(1, x - 1)],
    "Y": lambda x: [x for x in range(0, x)],
    "Z": lambda x: [len(x) for x in range(x)],
    "@": lambda x: prime_check(x),
    "-": lambda x: -(x - 1),
    "Ꮤ": lambda x: x.replace(" ", "").replace("\t", "").replace("\n", ""),
    "Ꮥ": lambda x: x.replace(" ", "").replace("\t", "").replace("\n", "").upper(),
}
nilads = {
    "á": "abcdefghijklmnopqrstuvwxyz",
    "Á": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "é": "abcdefghijklmnñopqrstuvwxyz",
    "É": "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
    "í": "qwertyuiopasdfghjklzxcvbnm",
    "Í": "QWERTYUIOPASDFGHJKLZXCVBNM",
    "ó": "0123456789",
    "Ó": "0123456789ABCDEF",
    "ú": "0123456789abcdefghijklmnopqrstuvwxyz",
    "Ú": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "ý": "0123456789abcdef",
    "Ý": code_page,
    "â": " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
    "Â": "\t \n",
    "ê": 10,
    "Ê": 0,
    "î": 256,
    "Î": -1,
}


tokens = []
for i in code:
    if i in [*monadiccommands, *dyadiccommands]:
        tokens.append(i)
    if i in [*nilads]:
        if type(nilads[i]) == str:
            tokens.append("ᐗ" + nilads[i] + "ᐓ")
        else:
            tokens.append(nilads[i])

arguments = []
argumentcount = sys.argv - 2
argindex = 0
for token in tokens:
    if token in [*monadiccommands]:
        if arguments == [] and argumentcount == 0:
            arguments.append(monadiccommands[token](0))
        elif arguments == [] and argumentcount > 0:
            arguments.append(monadiccommands[token](sys.argv[argindex]))
            argindex += 1
            try:sys.argv[argindex]
            except:argindex = 0
        elif len(arguments) > 1:
            arguments.append(monadiccommands[token](arguments[0]))
