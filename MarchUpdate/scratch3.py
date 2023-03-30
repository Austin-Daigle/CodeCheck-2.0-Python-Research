class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_node(root, path, value):
    if not path:
        return
    if path[0] in [child.value for child in root.children]:
        child = [child for child in root.children if child.value == path[0]][0]
    else:
        child = Node(path[0])
        root.children.append(child)
    add_node(child, path[1:], value)

def create_tree(a):
    root = Node('')
    for item in a:
        path = item.split()
        add_node(root, path, item)
    return root

def print_tree(node, prefix='', is_last_child=True):
    print(prefix, end='')
    if is_last_child:
        print('└─', end='')
        prefix += '   '
    else:
        print('├─', end='')
        prefix += '│  '
    print(node.value)
    for i, child in enumerate(node.children):
        is_last = i == len(node.children) - 1
        print_tree(child, prefix, is_last)

def compare_trees(tree1, tree2, path=[], shared_paths=[]):
    if tree1.value == tree2.value:
        path.append(tree1.value)
        for child1, child2 in zip(tree1.children, tree2.children):
            compare_trees(child1, child2, path, shared_paths)
        path.pop()
    else:
        if len(path) >= 2:
            shared_paths.append(path[:])
        for child1 in tree1.children:
            compare_trees(child1, tree2, [], shared_paths)
    return shared_paths



a = ['this ', ' a demo', 'this ', ' is here', ' cat', ' this ', ' is here']
b = ['this ', ' is here', ' dork', 'this ', 'cookie ', 'this ', ' is here']
print("tree a")
tree1 = create_tree(a)
print_tree(tree1)


print("")
print("tree b")
tree2 = create_tree(b)
print_tree(tree2)

print("analysis")
shared_paths = compare_trees(tree1, tree2)
print(shared_paths)