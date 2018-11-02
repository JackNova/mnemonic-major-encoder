"""
Dato un numero generare le possibili parole che lo codificano
"""
from mnemonic_major_encoder.encoder import encode
from collections import defaultdict
import sys
import json

WORDS_DICTIONARY_PATH = 'dictionaries/italungo.txt'
CACHED_ENCODED_WORDS = 'dictionaries/italungo-encoded.txt'
ENCODED_WORDS = defaultdict(list)

try:
    with open(CACHED_ENCODED_WORDS) as encoded_words_file:
        content = encoded_words_file.read()
        if content:
            ENCODED_WORDS = json.loads(content)
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except Exception:
    print("Unexpected error:", sys.exc_info()[0])

if not ENCODED_WORDS:
    with open(WORDS_DICTIONARY_PATH) as words_file:
        words = words_file.readlines()
        words_count = len(words)
        loaded_words = 0
        print(f"{words_count} words to load")
        for word in words:
            word = word.replace('\n', '')
            if word:
                number = encode(word)
                if number:
                    ENCODED_WORDS[number].append(word)
                else:
                    print("can't encode "+ word)
                loaded_words += 1
                if loaded_words % 10000 == 0:
                    print(f"{loaded_words}/{words_count}")
        print('dictionary loaded')
        with open(CACHED_ENCODED_WORDS, 'w+') as encoded_words_file:
            encoded_words_file.write(json.dumps(ENCODED_WORDS))


def decode(number):
    words = ENCODED_WORDS.get(number)
    if words:
        for word in words:
            print(word)
    return words
