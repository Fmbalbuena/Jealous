import sys
code_page = "|¬°!1\"2#3$4%5&6/7(8)9=0?'\\¿¡\tq@wertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM¨´+*~{}^`[],.-_:;<>éýúíóáÉÝÚÍÓÁèùìòàÈÙÌÒÀêûî"
code_page += "ôâÊÛÎÔÂ\nëÿüöïäËÜÖÏÄᐍᐎᐓᐗᎾᚁᚂᚃᚄᚅᚆᚇᚈᚉᚊᚋᚌᚍᚎᚏᏔᏕᏖᏗᏘᏙᏚᏛᏜᏝᏞᏟᏠᏡᏢᏣᏤᏥᏦᏧᏨᏩᏪᏫᏬᏭᏮᏯᏰᏱᏲᏳᏴᏵᏸᏹᏺᏻᏼᏽᎳᎴᎵᎶᎷᎸᎹᎺᎻᎼᎽᎿᏀᏁᏂᏃᏄᏅᏆᏇᏈᏉᏊᏋᏌᏍᏎᏏᏐᏑᏒᏓ×ĀāĂăĄąĆćĈĉĊċČčĎaĐ"
from sympy.ntheory.primetest import isprime as prime_check
"""
with open(sys.argv[1], 'rb') as file:
    code = file.read()
    code = "".join(code_page[i] for i in code)
"""
code = "ᐗHello, World!"
# Golfing language interpreter
lines = code.split("\n")
arguments = sys.argv[2:]
from math import gcd, lcm
dyadiccommands = {
    "×": lambda x, y: x * y,
    "Ꮎ": lambda x, y: x / y,
    "|": lambda x, y: x + y,
    "¬": lambda x, y: x - y,
    "°": lambda x, y: x % y,
    "#": lambda x, y: x ** y,
    "\\": lambda x, y: x // y,
    "\t": lambda x, y: x ** (1 / y),
    "a": lambda x, y: x.join(y),
    "b": lambda x, y: x.count(y),
    "c": lambda x, y: x.find(y),
    "d": lambda x, y: x.index(y),
    "e": lambda x, y: x[y],
    "f": lambda x, y: gcd(x, y),
    "g": lambda x, y: [x, y],
    "h": lambda x, y: lcm(x, y),
    "i": lambda x, y: x.replace(y, ""),
    "j": lambda x, y: x.split(y),
    "k": lambda x, y: x.strip(y),
    "l": lambda x, y: x.rstrip(y),
    "m": lambda x, y: x.lstrip(y),
    "n": lambda x, y: x,
    "ñ": lambda x, y: y,
    "o": lambda x, y: x,


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
    "ᚁ": lambda x: x.isupper(),
    "ᚂ": lambda x: x.islower(),
    "ᚃ": lambda x: x.isnumeric(),
    "ᚄ": lambda x: x.isalpha(),
    "ᚅ": lambda x: x.isalnum(),
    "Ꮤ": lambda x: x.replace(" ", "").replace("\t", "").replace("\n", ""),
    "Ꮥ": lambda x: x[-1],
    "Ꮦ": lambda x: [x],
    "Ꮧ": lambda x: x.conjugate(),
    "Ꮨ": lambda x: chr(x),
    "Ꮩ": lambda x: ord(x),
    "Ꮪ": lambda x: x % 2,
    "Ꮫ": lambda x: int(x % 2 == 0),
}
monadsdefaulttype = { # unused until [AI STARTS] is implemented
    "!": int,
    "A": str,
    "B": str,
    "C": str,
    "D": str,
    "E": int,
    "F": float,
    "G": list,
    "H": float,
    "I": int,
    "J": int,
    "K": float,
    "L": int,
    "M": int,
    "N": int,
    "Ñ": int,
    "O": int,
    "P": str,
    "Q": str,
    "R": str,
    "S": str,
    "T": str,
    "U": int,
    "V": int,
    "W": int,
    "X": int,
    "Y": int,
    "Z": int,
    "@": int,
    "-": int,
    "ᚁ": str,
    "ᚂ": str,
    "ᚃ": str,
    "ᚄ": str,
    "ᚅ": str,
    "Ꮤ": list,
    "Ꮥ": list,
    "Ꮦ": list,
    "Ꮧ": int,
    "Ꮨ": int,
    "Ꮩ": chr,
    "Ꮪ": int,
    "Ꮫ": int,
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

def Fizzbuzz():
    # Fizzbuzz
    global variable
    variable = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            variable += "FizzBuzz\n"
        elif i % 3 == 0:
            variable += "Fizz\n"
        elif i % 5 == 0:
            variable += "Buzz\n"
        else:
            variable += str(i) + "\n"

extendedNilads = {
    "k": {
        "A": "qwertyuiopasdfghjklñzxcvbnm",
        "B": "QWERTYUIOPASDFGHJKLÑZXCVBNM",
        "C": ":)",
        "D": ":D",
        "E": ":P",
        "F": Fizzbuzz(),
        "G": ":O",
        "H": "Hello, World!",
        "I": "UwU",
        "J": "\n".join(map(str, [i for i in range(1, 100)]))
    }
}


tokens = []
Read = True
for i in code:
    if not Read:
        if i == "ᐓ":
            Read = True
            continue
        continue
    if i in [*monadiccommands, *dyadiccommands]:
        tokens.append(i)
    if i in [*nilads]:
        if type(nilads[i]) == str:
            tokens.append("ᐗ" + nilads[i])
        else:
            tokens.append(nilads[i])
    if i == "ᐗ":
        # read until next "ᐓ" if there is one else implicitly read until end of line
        if "ᐓ" in code[code.index(i) + 1:]:
            tokens.append("ᐗ" + code[code.index(i) + 1:code.index("ᐓ")])
        else:
            tokens.append("ᐗ" + code[code.index(i) + 1:])
        # Continue until next "ᐓ"
        Read = False
arguments = []
argumentcount = len(sys.argv) - 1
argindex = 1
tokenindex = 0
while True:
    token = tokens[tokenindex]
    if token in [*monadiccommands]:
        if arguments == [] and argumentcount == 0:
            arguments.append(monadiccommands[token](0))
        elif arguments == [] and argumentcount > 0:
            arguments.append(monadiccommands[token](sys.argv[argindex]))
            argindex += 1
            try:sys.argv[argindex]
            except:argindex = 1
        elif len(arguments) > 0:
            arguments.append(monadiccommands[token](arguments.pop()))
    if token in [*dyadiccommands]:
        # Take next token as argument if is nilad
        tokenindex += 1
        if tokens[tokenindex][0] == "ᐗ":
            arguments.append(tokens[tokenindex][1:])
            arguments.append(dyadiccommands[token](arguments.pop(), arguments.pop()))
        else:
            if len(arguments) == 1:
                if argumentcount == 0:
                    arguments.append(dyadiccommands[token](arguments.pop(), 0))
                elif argumentcount > 0:
                    arguments.append(dyadiccommands[token](arguments.pop(), sys.argv[argindex]))
                    argindex += 1
                    try:sys.argv[argindex]
                    except:argindex = 1
            elif len(arguments) == 2:
                arguments.append(dyadiccommands[token](arguments.pop(), arguments.pop()))
    if token[0] == "ᐗ":
        arguments.append(token[1:])
    tokenindex += 1
    if tokenindex >= len(tokens):
        break
if len(arguments) != 0:
    print(end = arguments[0])
else:
    print(arguments.join("\n"))
