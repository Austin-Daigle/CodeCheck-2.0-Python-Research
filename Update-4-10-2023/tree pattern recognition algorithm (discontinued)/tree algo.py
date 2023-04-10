a = [[[0, 5], 'this '],
[[7, 14], ' a demo'],
[[15, 20], 'this '],
[[19, 27], ' is here'],
[[40, 43], ' cat'],
[[70, 74], ' this '],
[[90, 97], ' is here']]


b = [[[0, 5], 'this '],
[[10, 18], ' is here'],
[[50, 54], ' dork'],
[[60, 65], 'this '],
[[100, 107], 'cookie '],
[[100, 107], 'this '],
[[110, 117], ' is here']]

c = [x[1] for x in a]
d = [x[1] for x in b]
print(c)

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def print_tree(self, indent=0):
        if self.value is not None:
            print(' ' * indent + str(self.value))
        for child in self.children:
            child.print_tree(indent + 2)

    def print_tree_formatted(self, prefix=""):
        if self.value is not None:
            print(prefix + str(self.value))
        for i, child in enumerate(self.children):
            if i == len(self.children) - 1:
                child_prefix = prefix + "    "
                child_line_prefix = prefix + "└── "
            else:
                child_prefix = prefix + "│   "
                child_line_prefix = prefix + "├── "
            child.print_tree_formatted(child_prefix if child.children else child_line_prefix)

def create_tree(pattern_list):
    root = Node(None)
    for pattern in pattern_list:
        current_node = root
        for char in pattern:
            found_child = None
            for child in current_node.children:
                if child.value == char:
                    found_child = child
                    break
            if not found_child:
                found_child = Node(char)
                current_node.children.append(found_child)
            current_node = found_child
    return root

def find_shared_patterns(tree1, tree2):
    shared_patterns = []

    def _find_shared_patterns(node1, node2, current_pattern):
        if node1.value == node2.value:
            current_pattern.append(node1.value)
            for child1 in node1.children:
                for child2 in node2.children:
                    _find_shared_patterns(child1, child2, current_pattern.copy())

        if current_pattern and not node1.children and not node2.children:
            shared_patterns.append("".join(current_pattern))

    for child1 in tree1.children:
        for child2 in tree2.children:
            _find_shared_patterns(child1, child2, [])

    return shared_patterns

def compare_lists(list1, list2):
    tree1 = create_tree(list1)
    tree2 = create_tree(list2)

print(find_shared_patterns(create_tree(c), create_tree(d)))

dummy = create_tree(c)
dummy.print_tree_formatted()