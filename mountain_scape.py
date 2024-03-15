# https://py.checkio.org/en/mission/mountain-scape/
# https://py.checkio.org/mission/mountain-scape/publications/tokiojapan55/python-3/first/?ordering=most_voted&filtering=all


def mountain_scape(tops):
    triangles = set()
    for top_x, top_y in tops:
        for rows_from_top in range(top_y):
            row_triangles = {(x, top_y - rows_from_top) 
                for x in range(top_x - rows_from_top, top_x + rows_from_top + 1)}
            triangles |= row_triangles
    return len(triangles)
