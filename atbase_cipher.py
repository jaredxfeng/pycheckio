import re 


def atbash(plaintext: str) -> str:
    out = ""
    for char in plaintext:
        if re.match("[a-z]", char):
            out += chr(ord("z") + ord("a") - ord(char))
        elif re.match("[A-Z]", char):
            out += chr(ord("Z") + ord("A") - ord(char))
        else:
            out += char
    return out
