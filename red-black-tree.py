BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'


class Node:
    def __init__(self, value, color, parent, left=None, right=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.color} {self.value} Node'

    def has_children(self) -> bool:
        return bool(self.get_children_count())

    def get_children_count(self) -> int:
        if self.color == NIL:
        return 0
    return sum([int(self.left.color != NIL), int(self.right.color != NIL)])


class RBTree:
    NIL_LEAF = Node(value=None, color=NIL, parent=None)
    def __init__(self):
        self.count = 0
        self.root = None
        self.ROTATIONS = {
            'L': self.right_rotation,
            
            'R': self.left_rotation
        }

    def __iter__(self):
        if not self.root:
        return list()
        yield from self.root.__iter__()

    def add_node(self, value):
        if not self.root:
            self.root = Node(value, color=BLACK, parent=None,
                            left=self.NIL_LEAF, right=self.NIL_LEAF)
            self.count += 1
            return
            parent, node_dir = self.find_parent(value)
            
        if node_dir is None:
            return
            new_node = Node(value=value, color=RED, parent=parent,
                            left=self.NIL_LEAF, right=self.NIL_LEAF)
            if node_dir == 'L':
                parent.left = new_node
            else:
                parent.right = new_node

            self.try_rebalance(new_node)
            self.count += 1
    def find_parent(self, value):
        def inner_find(parent):
            if value == parent.value:
                return None, None
            elif parent.value < value:
                if parent.right.color == NIL:
                    return parent, 'R'
    return inner_find(parent.right)

    elif parent.value > value:
        if parent.left.color == NIL:
            return parent, 'L'
            return inner_find(parent.left)
            return inner_find(self.root)
        
    def try_rebalance(self, node):
        parent = node.parent
        value = node.value
        if (parent is None or parent.parent is None or
                (node.color != RED or parent.color != RED)):
        return
        grandfather = parent.parent
        node_dir = 'L' if parent.value > value else 'R'
        parent_dir = 'L' if grandfather.value > parent.value else 'R'
        uncle = grandfather.right if parent_dir == 'L' else grandfather.left
        general_direction = node_dir + parent_dir

        if uncle == self.NIL_LEAF or uncle.color == BLACK:
            if general_direction == 'LL':
            self.right_rotation(node, parent, grandfather, to_recolor=True)
        elif general_direction == 'RR':
            self.left_rotation(node, parent, grandfather, to_recolor=True)
            elif general_direction == 'LR':
            self.right_rotation(node=None, parent=node, grandfather=parent)
            self.left_rotation(node=parent, parent=node,
                        grandfather=grandfather, to_recolor=True)
        
        elif general_direction == 'RL':
            self.left_rotation(node=None, parent=node, grandfather=parent)
            self.right_rotation(node=parent, parent=node, grandfather=grandfather,
                            to_recolor=True)

        else:
            raise Exception(f'{general_direction} is not a valid direction!')
            else:
                self.recolor(grandfather)
                def update_parent(self, node, parent_old_child, new_parent):
                node.parent = new_parent
            if new_parent:
                if new_parent.value > parent_old_child.value:
                new_parent.left = node
            else:
                new_parent.right = node
            else:
                self.root = node
        
        def right_rotation(self, node, parent, grandfather, to_recolor=False):
            grand_grandfather = grandfather.parent
            self.update_parent(node=parent, parent_old_child=grandfather,
                            new_parent=grand_grandfather)
            old_right = parent.right
            parent.right = grandfather
            grandfather.parent = parent
            grandfather.left = old_right
            old_right.parent = grandfather
            if to_recolor:
                parent.color = BLACK
                node.color = RED
                grandfather.color = RED

        def left_rotation(self, node, parent, grandfather, to_recolor=False):
            grand_grandfather = grandfather.parent
            self.update_parent(node=parent, parent_old_child=grandfather,
                            new_parent=grand_grandfather)

    old_left = parent.left
    parent.left = grandfather
    grandfather.parent = parent
    grandfather.right = old_left
    old_left.parent = grandfather
    if to_recolor:
        parent.color = BLACK
        node.color = RED
        grandfather.color = RED

    def recolor(self, grandfather):
        grandfather.right.color = BLACK
        grandfather.left.color = BLACK
        if grandfather != self.root:
            grandfather.color = RED
        self.try_rebalance(grandfather)


    def find_node(self, value):
        def inner_find(root):
            if root is None or root == self.NIL_LEAF:
                return None
            if value > root.value:
                return inner_find(root.right)
            elif value < root.value:
                return inner_find(root.left)
            else:
                return root
            found_node = inner_find(self.root)
        return found_node

    def in_order(self, start, traversal):
        if start:
            traversal = self.in_order(start.left, traversal)
            if start.value != None:
                traversal += str(start.value) + ' '
                traversal = self.in_order(start.right, traversal)
                return traversal


def main():
    rb_tree = RBTree()
    rb_tree.add_node(10)
    rb_tree.add_node(20)
    rb_tree.add_node(4)
    rb_tree.add_node(15)
    rb_tree.add_node(17)
    rb_tree.add_node(40)
    rb_tree.add_node(50)
    rb_tree.add_node(60)
    res = rb_tree.in_order(rb_tree.root, '')
    res = res.split(' ')
    del res[-1]
    res = ' -> '.join(res)
    print(f'Inorder traversal of this red-black : {res}')


if __name__ == '__main__':
    main()
