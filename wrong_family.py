# https://py.checkio.org/en/mission/wrong-family/
from anytree import Node


def is_family(tree):
    nodes = {}
    for [parent, child] in tree:
        if parent == child:
            return False
        if parent not in nodes:
            nodes[parent] = Node(parent)
        if child not in nodes:
            nodes[child] = Node(child, parent=nodes[parent])
        else:
            if nodes[child] in nodes[parent].ancestors \
            or nodes[child] in nodes[parent].siblings \
            or nodes[parent] in nodes[child].siblings \
            or nodes[child].parent is not None:
                return False
            nodes[child].parent = nodes[parent]

    roots = find_all_roots(nodes)
    if len(roots) > 1:
        return False
    
    return True


def find_all_roots(nodes):
    roots = set()
    for _, node in nodes.items():
        if node.root not in roots:
            roots.add(node.root)
    return roots


assert is_family([["Logan", "Jack"], ["Logan", "Jack"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Alexander"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Logan"]]) == False
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Jack"]]) == False
assert (
    is_family([["Logan", "William"], ["Logan", "Jack"], ["Mike", "Alexander"]]) == False
)
assert is_family([["Jack", "Mike"], ["Logan", "Mike"], ["Logan", "Jack"]]) == False
assert is_family([['Logan', 'William'], ['Logan', 'Jack'], ['Mike', 'Mike']]) == False
assert is_family([['Logan', 'William'], ['William', 'Jack'], ['Jack', 'Mike'], ['Mike', 'Alexander']]) == True
assert is_family([['Logan', 'William'], ['Mike', 'Alexander'], ['William', 'Alexander']]) == False
assert is_family([['Logan', 'Mike'], ['Alexander', 'Jack'], ['Jack', 'Alexander']]) == False
assert is_family([['Logan', 'Mike'], ['Alexander', 'Jack'], ['Jack', 'Logan']]) == True
assert is_family([['Logan', 'Mike'], ['Alexander', 'Jack'], ['Jack', 'Logan'], ['Alex', 'Bob']]) == False
assert is_family([['Logan', 'Mike'], ['Alexander', 'Jack'], ['Mike', 'Alexander']]) == True
