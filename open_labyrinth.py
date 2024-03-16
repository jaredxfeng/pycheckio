# https://py.checkio.org/en/mission/open-labyrinth/

from typing import List
import numpy as np


class Node:
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords
        self.next = {}
        self.next["E"] = self.next["S"] = self.next["W"] = \
            self.next["N"] = None
        
    def __repr__(self):
        return f"Node('{self.name}')"


def checkio(maze_map: List[List[int]]) -> str:
    maze_map = np.array(maze_map)
    node = Node("", coords=np.array([1, 1]))
    directions = {(0, 1): "E", (1, 0): "S", (0, -1): "W", (-1, 0): "N"}
    goal = np.array([10, 10])
    steps = ""
    queue = [node]
    while queue != []:
        for d_coords, direction in directions.items():
            candidate = node.coords + d_coords
            if maze_map[tuple(candidate)] == 0:
                node.next[direction] = Node(node.name + direction,
                    coords=candidate)
                queue.append(node.next[direction])
        node = queue.pop(0)
        maze_map[tuple(node.coords)] = -1
        if all(node.coords == goal):
            steps = node.name
            break
    return steps
