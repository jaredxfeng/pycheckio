# https://py.checkio.org/en/mission/chess-knight/
def valid_new_pos(horse, dir_x, dir_y):
    x_in_range = ord("a") <= ord(horse[0]) + dir_x <= ord("h")
    y_in_range = 1 <= int(horse[1]) + dir_y <= 8
    return x_in_range and y_in_range 


def get_new_pos(horse, dir_x, dir_y):
    return chr(ord(horse[0]) + dir_x) \
                    + str(int(horse[1]) + dir_y)


def chess_knight(start, moves):
    cells = set()
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1)]
    directions += [(-x, -y) for (x, y) in directions]
    queue = [(start, 0)]
    while queue:
        horse, move_cnt = queue.pop(0)
        if move_cnt > 0:
            cells.add(horse)
        if move_cnt < moves:
            for dir_x, dir_y in directions:
                if valid_new_pos(horse, dir_x, dir_y):
                    horse_new_pos = get_new_pos(horse, dir_x, dir_y)
                    queue.append((horse_new_pos, move_cnt + 1))
    return sorted(cells, key=lambda x: (x[0], x[1]))
