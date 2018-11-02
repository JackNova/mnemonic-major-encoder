import re
from unidecode import unidecode
from string import whitespace
import codecs

WHITESPACE = whitespace
VOWELS = set('aeiouhy')
BUFFER_SIZE = 10
CODES = [re.compile(pattern) for pattern in [
    "sc[ei]|ss?|zz?", # 0
    "tt?|dd?", # # 1
    "nn|g?n", # 2
    "mm?", # 3
    "rr?", # 4
    "ll|g?l", # 5
    "(cc?|gg?)[ei]|j", # 6
    "c[khq]|cc?|gg?|qq?|kk?", # 7
    "ff?|vv?", # 8
    "pp?|bb?" # 9
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
