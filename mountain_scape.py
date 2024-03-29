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


assert mountain_scape([[1,1],[4,2],[7,3]]) == 13
assert mountain_scape([[0,2],[5,3],[7,5]]) == 29
assert mountain_scape([[1,3],[5,3],[5,5],[8,4]]) == 37
assert mountain_scape([[3,3],[5,3],[7,3],[9,3],[11,3],[13,3],[15,3],[17,3],[19,3],[21,3]]) == 54
assert mountain_scape([[5,5],[7,5],[9,5],[11,5],[13,5],[15,5],[17,5],[19,5],[21,5],[23,5],[25,5],[27,5],[29,5],[31,5],[33,5]]) == 151
assert mountain_scape([[10,10],[12,10],[14,10],[16,10],[18,10],[20,10],[22,10],[24,10],[26,10],[28,10],[30,10],[32,10],[34,10],[36,10],[38,10],[40,10],[42,10],[44,10],[46,10],[48,10],[50,10],[52,10],[54,10],[56,10],[58,10],[60,10],[62,10],[64,10],[66,10],[68,10]]) == 651
assert mountain_scape([[7,13]]) == 169
assert mountain_scape([[23,9],[69,3]]) == 90
assert mountain_scape([[44,18],[3,17],[39,9]]) == 613
assert mountain_scape([[26,2],[86,6],[65,5],[45,25]]) == 661
assert mountain_scape([[40,40],[66,26],[81,23],[58,34],[44,8]]) == 2212
assert mountain_scape([[95,7],[74,12],[89,3],[98,2],[97,21],[2,28]]) == 1344
assert mountain_scape([[7,3],[44,12],[59,15],[42,8],[19,27],[63,5],[73,3]]) == 1018
assert mountain_scape([[9,3],[11,5],[17,13],[81,7],[21,9],[0,6],[34,6],[41,7],[43,29],[7,19]]) == 1235
assert mountain_scape([[29,27],[96,20],[48,30],[7,11],[1,19],[2,24],[94,20],[39,5],[19,33],[82,14],[8,22],[51,11],[75,13],[21,17],[78,2]]) == 2427
assert mountain_scape([[42,22],[17,7],[64,16],[22,2],[64,4],[10,16],[84,10],[6,40],[22,2],[87,11],[75,13],[66,34],[98,4],[74,2],[45,1],[90,36],[91,5],[6,6],[64,26],[75,7]]) == 3582
assert mountain_scape([[54,2],[1,1],[90,4],[45,29],[58,16],[9,1],[46,22],[15,13],[0,4],[90,36],[41,17],[63,7],[93,7],[92,38],[21,25],[2,2],[43,27],[88,12],[61,3],[54,24],[47,33],[78,24],[18,16],[23,35],[16,2]]) == 3105
assert mountain_scape([[19,15],[14,2],[37,1],[64,14],[22,26],[68,34],[8,10],[97,19],[13,5],[22,8],[49,7],[12,2],[93,13],[27,39],[78,26],[48,4],[44,10],[100,8],[98,8],[33,7],[81,9],[21,29],[20,48],[38,38],[34,12],[53,39],[35,23],[15,5],[74,2],[50,22]]) == 3710
assert mountain_scape([[90,12],[87,45],[25,19],[54,4],[49,7],[24,26],[27,11],[59,1],[29,13],[79,3],[0,2],[76,4],[53,7],[10,2],[80,8],[35,9],[4,12],[81,13],[61,13],[25,3],[17,25],[71,7],[43,5],[74,36],[99,9],[78,36],[61,13],[97,17],[76,4],[47,5],[45,9],[45,9],[97,19],[73,3],[32,2]]) == 2950
assert mountain_scape([[52,6],[33,9],[33,31],[2,4],[100,20],[34,18],[23,1],[88,18],[47,1],[49,29],[51,35],[86,14],[50,26],[26,4],[81,41],[97,5],[4,10],[33,5],[81,5],[33,1],[3,23],[92,26],[69,37],[80,2],[20,2],[12,10],[56,14],[75,19],[30,40],[81,9],[53,23],[73,5],[69,11],[87,21],[91,3],[92,4],[53,11],[18,32],[43,47],[45,5]]) == 3813
assert mountain_scape([[20,2],[60,10],[87,37],[56,26],[2,6],[43,31],[60,26],[10,14],[23,13],[96,22],[70,36],[31,15],[23,21],[29,17],[49,1],[51,25],[0,2],[74,10],[65,7],[29,39],[22,2],[57,23],[22,2],[55,23],[49,1],[26,4],[45,9],[11,5],[55,7],[53,1],[59,31],[35,1],[1,1],[1,45],[22,6],[59,13],[27,31],[90,16],[37,5],[20,12],[5,7],[87,25],[78,8],[40,2],[7,27]]) == 4470
assert mountain_scape([[81,1],[7,5],[44,16],[77,11],[58,34],[94,8],[31,3],[64,2],[20,32],[60,4],[58,8],[74,22],[58,12],[7,15],[58,8],[19,7],[69,15],[48,14],[59,15],[15,9],[17,37],[95,13],[57,13],[92,18],[27,9],[45,27],[52,8],[45,1],[48,8],[39,5],[49,3],[30,4],[92,6],[46,28],[26,4],[90,32],[20,8],[46,20],[48,6],[25,5],[29,21],[90,6],[31,13],[46,26],[27,9],[64,10],[68,36],[49,3],[30,8],[37,25]]) == 3275
assert mountain_scape([[85,7],[59,9],[22,2],[14,2],[27,3],[6,26],[6,24],[100,8],[8,6],[73,21],[88,24],[90,46],[35,33],[74,10],[93,9],[37,35],[70,8],[99,41],[52,8],[96,6],[50,28],[50,12],[34,2],[68,10],[22,2],[57,1],[55,1],[87,31],[29,5],[22,26],[58,10],[62,12],[50,18],[23,1],[26,34],[88,22],[46,16],[83,1],[22,6],[53,23],[6,2],[63,1],[7,37],[68,8],[21,1],[95,5],[46,36],[74,22],[12,36],[17,7]]) == 4515
assert mountain_scape([[45,17],[2,24],[77,5],[69,1],[36,8],[51,27],[84,6],[74,8],[61,23],[40,4],[20,18],[75,9],[82,6],[50,20],[100,14],[77,15],[0,14],[82,6],[14,4],[79,1],[25,17],[71,21],[27,13],[79,7],[69,5],[66,2],[74,24],[96,2],[58,2],[86,22],[63,11],[58,22],[68,12],[54,20],[57,1],[75,39],[67,17],[24,16],[76,32],[49,7],[69,13],[6,26],[40,6],[0,8],[44,22],[92,14],[49,31],[30,10],[63,3],[97,11]]) == 2740
assert mountain_scape([[49,29],[22,12],[30,24],[10,36],[86,2],[68,4],[100,28],[17,7],[72,8],[30,14],[52,38],[1,3],[2,6],[95,15],[58,6],[6,10],[35,5],[36,12],[4,2],[32,36],[47,13],[83,31],[64,12],[60,8],[57,1],[81,7],[53,19],[67,15],[8,40],[98,10],[41,29],[51,41],[11,1],[62,20],[63,17],[62,32],[30,8],[62,4],[37,7],[100,2],[83,39],[11,1],[59,45],[17,43],[8,26],[30,28],[41,3],[87,13],[74,10],[55,3]]) == 4476
assert mountain_scape([[82,10],[33,33],[44,14],[91,5],[23,3],[48,14],[25,17],[35,3],[84,24],[99,5],[88,10],[42,16],[10,16],[11,3],[0,6],[29,1],[11,1],[85,5],[66,2],[42,4],[25,33],[36,8],[6,2],[22,10],[40,8],[81,33],[57,23],[60,10],[33,11],[77,15],[28,10],[72,4],[77,7],[10,2],[75,17],[19,5],[8,18],[61,21],[41,15],[28,2],[68,40],[69,1],[60,10],[26,40],[32,4],[58,4],[26,6],[88,12],[14,4],[28,32]]) == 3028

