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


def visit(_node, _res):
    _res.append(_node)


def pre_order(_tree: Node, res: list):
    if _tree is not None:
        visit(_tree, res)
        pre_order(_tree.left, res)
        pre_order(_tree.right, res)


def in_order(_tree: Node, res: list):
    if _tree is not None:
        in_order(_tree.left, res)
        visit(_tree, res)
        in_order(_tree.right, res)


def post_order(_tree: Node, res: list):
    if _tree is not None:
        post_order(_tree.left, res)
        post_order(_tree.right, res)
        visit(_tree, res)


print("pre_order")
pre_order_res = []
pre_order(tree, pre_order_res)
[print(_node) for _node in pre_order_res]


print("in_order")
in_order_res = []
in_order(tree, in_order_res)
[print(_node) for _node in in_order_res]


print("post_order")
post_order_res = []
post_order(tree, post_order_res)
[print(_node) for _node in post_order_res]
