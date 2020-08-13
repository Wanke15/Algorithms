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


def mid_order(_tree: Node, res: list):
    if _tree is not None:
        mid_order(_tree.left, res)
        visit(_tree, res)
        mid_order(_tree.right, res)


def post_order(_tree: Node, res: list):
    if _tree is not None:
        post_order(_tree.left, res)
        post_order(_tree.right, res)
        visit(_tree, res)


print("pre_order: ")
pre_order_res = []
pre_order(tree, pre_order_res)
[print(_node) for _node in pre_order_res]


print("in_order: ")
mid_order_res = []
mid_order(tree, mid_order_res)
[print(_node) for _node in mid_order_res]


print("post_order: ")
post_order_res = []
post_order(tree, post_order_res)
[print(_node) for _node in post_order_res]


def reconstruct_from_pre_and_mid(pre_order_seq: list, mid_order_seq: list):
    # 叶子节点的情况
    if len(pre_order_seq) == 0:
        return None

    # 根节点
    root_node = pre_order_seq[0]

    # 确定根节点在中序遍历中的位置
    root_pos_in_mid = 0
    for i in range(len(mid_order_seq)):
        if mid_order_seq[i] == root_node:
            root_pos_in_mid = i
            break

    # 确定两种遍历的左右子树，递归
    left = reconstruct_from_pre_and_mid(pre_order_seq[1: root_pos_in_mid+1], mid_order_seq[:root_pos_in_mid])
    right = reconstruct_from_pre_and_mid(pre_order_seq[root_pos_in_mid+1:], mid_order_seq[root_pos_in_mid+1:])

    root_node.left = left
    root_node.right = right
    return root_node


print("Reconstruct from pre and mid order: ")
new_tree = reconstruct_from_pre_and_mid(pre_order_res, mid_order_res)
print(new_tree == tree)
new_tree_post_order_res = []
post_order(new_tree, new_tree_post_order_res)
[print(_node) for _node in new_tree_post_order_res]


def reconstruct_from_post_and_mid(post_order_seq: list, mid_order_seq: list):
    # 叶子节点的情况
    if len(post_order_seq) == 0:
        return None
    # 根节点
    root_node = post_order_seq[-1]

    # 确定根节点在中序遍历中的位置
    root_pos_in_mid = 0
    for i in range(len(mid_order_seq)):
        if mid_order_seq[i] == root_node:
            root_pos_in_mid = i
            break

    # 确定两种遍历的左右子树，递归
    left = reconstruct_from_post_and_mid(post_order_seq[: root_pos_in_mid], mid_order_seq[:root_pos_in_mid])
    right = reconstruct_from_post_and_mid(post_order_seq[root_pos_in_mid: -1], mid_order_seq[root_pos_in_mid+1:])

    root_node.left = left
    root_node.right = right
    return root_node


print("Reconstruct from post and mid order: ")
new_tree = reconstruct_from_post_and_mid(post_order_res, mid_order_res)
print(new_tree == tree)
new_tree_pre_order_res = []
pre_order(new_tree, new_tree_pre_order_res)
[print(_node) for _node in new_tree_pre_order_res]
