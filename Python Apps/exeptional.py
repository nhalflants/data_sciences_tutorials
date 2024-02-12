import sys

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4'
}


def convert(s):
    """Convert a string to an integer"""
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}",file=sys.stderr)
        raise