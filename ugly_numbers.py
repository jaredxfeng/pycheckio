# https://py.checkio.org/en/mission/ugly-numbers/
from math import log, ceil


def ugly_number(n: int) -> int:
    if n <= 6:
        return n
    ugly_numbers = list(range(1, 7))
    last_ugly_number = ugly_numbers[-1]
    staging = set()
    while len(ugly_numbers) < n:
        for factor in [2, 3, 5]:
            if last_ugly_number % factor:
                staging.add(
                    factor**ceil(log(last_ugly_number)/log(factor))
                )
            else:
                staging.add(
                    ugly_numbers[
                        ugly_numbers.index(last_ugly_number/factor) + 1
                    ]*factor
                )
        last_ugly_number = ugly_number = min(list(staging))
        staging.remove(ugly_number)
        ugly_numbers.append(ugly_number)
    return ugly_numbers[-1]


assert ugly_number(4) == 4
assert ugly_number(6) == 6
assert ugly_number(15) == 11
assert ugly_number(1) == 1
assert ugly_number(29) == 75
assert ugly_number(84) == 960
assert ugly_number(171) == 9216
assert ugly_number(313) == 100000
assert ugly_number(593) == 2332800
assert ugly_number(899) == 26214400
assert ugly_number(1173) == 150000000
assert ugly_number(1398) == 512000000
assert ugly_number(1407) == 536870912
assert ugly_number(1500) == 859963392

