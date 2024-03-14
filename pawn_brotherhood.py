# https://py.checkio.org/en/mission/pawn-brotherhood/

def get_guardian_squares(pawn: str) -> set:
    pawn_x, pawn_y = pawn[0], int(pawn[1])
    x_left = chr(ord(pawn_x) - 1)
    x_right = chr(ord(pawn_x) + 1)
    return {x_coord + str(pawn_y - 1) for x_coord in [x_left, x_right]}

def safe_pawns(pawns: set):
    safe_count = 0
    for pawn in pawns:
        guardian_squares = get_guardian_squares(pawn)
        if len(pawns.intersection(guardian_squares)) > 0:
            safe_count += 1
    return safe_count
