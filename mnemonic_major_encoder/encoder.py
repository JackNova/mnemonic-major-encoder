import re
from unidecode import unidecode
from string import whitespace

WHITESPACE = whitespace
VOWELS = set('aeiouhy')
BUFFER_SIZE = 10
CODES = [re.compile(pattern) for pattern in [
    "sc[ei]|ss?|zz?",
    "tt?|dd?",
    "nn|g?n",
    "mm?",
    "rr?",
    "ll|g?l",
    "(cc?|gg?)[ei]|j",
    "c[khq]|cc?|gg?|qq?|kk?",
    "ff?|vv?",
    "pp?|bb?"
]]


def encode(text: str):
    rest = unidecode(text.lower())
    result = ""
    while rest:
        if rest[0] in VOWELS:
            rest = rest[1:] if len(rest) > 1 else None
            continue
        for idx, matcher in enumerate(CODES):
            match = matcher.match(rest)
            if match:
                result += str(idx)
                _, end = match.span()
                rest = rest[end:]
                break
        else:
            if len(rest) > 0:
                result += rest[0]
                rest = rest[1:] if len(rest) > 1 else None
    return result
