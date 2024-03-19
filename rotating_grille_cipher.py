# https://py.checkio.org/en/mission/rotating-grille-cipher/
from typing import List, Optional
import numpy as np


def grille_encrypt(plaintext: str, grille: List[str]) -> Optional[str]:
    grille = np.array([list(row) for row in grille])
    out_str = ""
    for i in range(len(plaintext) // 16):
        mask = grille
        grid = np.empty([4, 4], dtype=str)
        for j in range(4):
            try:
                grid[mask == "X"] = list(plaintext[16*i + 4*j:16*i + 4*j + 4])
            except:
                return None
            mask = np.rot90(mask, k=-1)
        if (grid == "").any().any():
            return None
        out_str += "".join(grid.flatten())

    return out_str
