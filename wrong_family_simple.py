#https://py.checkio.org/en/mission/wrong-family/

def is_family(tree: list[list[str]]) -> bool:
    dads = []
    sons = []

    for dad, son in tree:
        dads += [dad]
        if son in sons:
            return False
        sons += [son]
        if [son, dad] in tree:
            return False

    fatherless = 0
    for dad in set(dads):
        if dad not in sons:
            fatherless += 1
            if fatherless > 1:
                return False

    return True
