class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "{}".format(self.data)


def build_tree():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    c.left = f

    return a


tree = build_tree()


def visit(_node):
    print(_node)


def pre_order(_tree: Node):
    if _tree is not None:
        visit(_tree)
        pre_order(_tree.left)
        pre_order(_tree.right)


def in_order(_tree: Node):
    if _tree is not None:
        in_order(_tree.left)
        visit(_tree)
        in_order(_tree.right)


def post_order(_tree: Node):
    if _tree is not None:
        post_order(_tree.left)
        post_order(_tree.right)
        visit(_tree)


print("pre_order")
pre_order(tree)


print("in_order")
in_order(tree)

print("post_order")
post_order(tree)
