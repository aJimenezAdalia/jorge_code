

import json

NUMBERS = (128, 64, 32, 16, 8, 4, 2, 1)

def evaluate_ip(ip: str) -> str:
    if len(ip) > 15:
        return 'binary'
    return 'decimal'


def text_to_json(text: str) -> dict:
    pass
