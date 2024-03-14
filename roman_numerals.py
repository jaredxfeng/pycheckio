# https://py.checkio.org/mission/roman-numerals/

def checkio(num):
    out = ""
    num = str(num)
    romans = {
        3: {"five": "", "one": "M"}, 2: {"five": "D", "one": "C"}, 
        1: {"five": "L", "one": "X"}, 0: {"five": "V", "one": "I"}
    }
    curr_digit = lambda i: int(num[i])

    for i in range(len(num)):
        pow_10 = len(num) - i - 1 # pow_10: power of 10
        if curr_digit(i) == 4:
            out += romans[pow_10]["one"] + romans[pow_10]["five"]
        elif curr_digit(i) == 9:
            out += romans[pow_10]["one"] + romans[pow_10 + 1]["one"]
        else:
            if curr_digit(i) >= 5:
                out += romans[pow_10]["five"]
            out += romans[pow_10]["one"]*(curr_digit(i) % 5)
    return out


if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
