# https://py.checkio.org/en/mission/scytale-encryption/
from typing import Optional


def scytale_decipher(ciphertext: str, crib: str) -> Optional[str]:
    out = None
    for key in range(1, len(ciphertext) + 1):
        deciphered = ""
        for row in range(key):
            deciphered += ciphertext[row:len(ciphertext):key]
        if crib in deciphered:
            if out is None:
                out = deciphered
            else:
                return None
    return out
