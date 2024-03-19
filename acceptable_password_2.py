# https://py.checkio.org/en/mission/acceptable-password-ii/
import re

def is_acceptable_password(password: str) -> bool:
    has_digit = re.search(r"\d", password)
    return bool(has_digit) and len(password) > 6
