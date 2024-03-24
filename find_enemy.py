# https://py.checkio.org/en/mission/find-enemy/
from typing import List, Optional
from collections import Counter


def is_in_even_col(you):
    return (ord(you[0]) - ord("A")) % 2


class Node:
    def __init__(self, hex, running_steps):
        self.hex = hex
        self.running_steps = running_steps


def get_next_hex(hex, dir):
    match dir:
        case "N":
            if hex[1] == "1":
                return None
            return hex[0] + str(int(hex[1]) - 1)
        case "S":
            if hex[1] == "9":
                return None
            return hex[0] + str(int(hex[1]) + 1)
        case "NE":
            if hex[0] == "Z" or (not is_in_even_col(hex) and hex[1] == "1"):
                return None
            return chr(ord(hex[0]) + 1) + (hex[1] if is_in_even_col(hex) else str(int(hex[1]) - 1))
        case "SE":
            if hex[0] == "Z" or (is_in_even_col(hex) and hex[1] == "9"):
                return None
            return chr(ord(hex[0]) + 1) + (hex[1] if not is_in_even_col(hex) else str(int(hex[1]) + 1))
        case "NW":
            if hex[0] == "A" or (not is_in_even_col(hex) and hex[1] == "1"):
                return None
            return chr(ord(hex[0]) - 1) + (hex[1] if is_in_even_col(hex) else str(int(hex[1]) - 1))
        case "SW":
            if hex[0] == "A" or (is_in_even_col(hex) and hex[1] == "9"):
                return None
            return chr(ord(hex[0]) - 1) + (hex[1] if not is_in_even_col(hex) else str(int(hex[1]) + 1))


def get_steps_to_enemy_bfs(you, enemy):
    queue = [Node(you, [])]
    visited = {you}
    dirs = ["N", "NE", "SE", "S", "SW", "NW"]
    while queue:
        node = queue.pop(0)
        if node.hex == enemy:
            return node.running_steps
        for dir in dirs:
            next_hex = get_next_hex(node.hex, dir)
            next_running_steps = node.running_steps.copy() + [dir]
            if next_hex is not None and next_hex not in visited:
                queue.append(Node(next_hex, next_running_steps))
                visited.add(next_hex)
    return "IDK"


def get_relative_steps(steps, dir):
    dirs = ["N", "NE", "SE", "S", "SW", "NW"]
    i = dirs.index(dir)
    dirs_rotated = dirs[i:] + dirs[:-(6 - i)]
    dir_map = {direction: new_direction 
        for new_direction, direction in zip(dirs, dirs_rotated)}
    relative_steps = [dir_map[step] for step in steps]
    return relative_steps


def get_sector(relative_steps):
    cnt = Counter(relative_steps)
    if cnt["N"] > cnt["SE"] and cnt["N"] > cnt["SW"]:
        return "F"
    elif cnt["S"] > cnt["NE"] and cnt["S"] > cnt["NW"]:
        return "B"
    elif (cnt["SE"] > cnt["N"] or cnt["NE"] > cnt["S"]) \
        and cnt["SW"] + cnt["NW"] == 0:
        return "R"
    elif (cnt["SW"] > cnt["N"] or cnt["NW"] > cnt["S"]) \
        and cnt["SE"] + cnt["NE"] == 0:
        return "L"
    return "IDK"


def find_enemy(you: str, dir: str, enemy: str):
    steps = get_steps_to_enemy_bfs(you, enemy)
    relative_steps = get_relative_steps(steps, dir)
    sector = get_sector(relative_steps)
    return [sector, len(steps)]


assert find_enemy("G5", "N", "G4") == ["F", 1]
assert find_enemy("G5", "N", "I4") == ["R", 2]
assert find_enemy("G5", "N", "J6") == ["R", 3]
assert find_enemy("G5", "N", "G9") == ["B", 4]
assert find_enemy("G5", "N", "B7") == ["L", 5]
assert find_enemy("G5", "N", "A2") == ["L", 6]
assert find_enemy("G3", "NE", "C5") == ["B", 4]
assert find_enemy("H3", "SW", "E2") == ["R", 3]
assert find_enemy("A4", "S", "M4") == ["L", 12]
assert find_enemy("D9", "NE", "B9") == ["B", 2]
assert find_enemy("B2", "N", "C4") == ["B", 2]
assert find_enemy('C3', 'SE', 'A1') == ['B', 3]
assert find_enemy('D3', 'NE', 'A1') == ['L', 4]
assert find_enemy('A1', 'SW', 'Z9') == ['B', 25]
