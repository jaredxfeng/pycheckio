# https://py.checkio.org/en/mission/acceptable-password-vi/

import re
def is_acceptable_password(password: str) -> bool:
    has_digit = re.search(r"\d", password)
    has_non_digit = re.search(r"\D", password)
    return ((has_digit and has_non_digit and len(password) > 6) \
        or len(password) > 9) and "password" not in password \
        and "PASSWORD" not in password and len(set(password)) >= 3
