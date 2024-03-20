# https://py.checkio.org/en/mission/boolean-algebra/


def boolean(x: bool, y: bool, operation: str) -> bool:
    match operation:
        case "conjunction":
            return x and y
        case "disjunction":
            return x or y
        case "implication":
            return not x or y
        case "exclusive":
            return (x and not y) or (y and not x)
        case "equivalence":
            return (x and y) or (not x and not y)
