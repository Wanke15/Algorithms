class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{}".format(self.val)

    def __eq__(self, other):
        if self.val == other.val:
            if self.left == other.left and self.right == other.right:
                return True
            else:
                return False
        else:
            return False


def build_tree():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    c.left = f

    return a


tree = build_tree()

if __name__ == '__main__':

    def visit(_node, _res):
        _res.append(_node)


    def pre_order(_tree: TreeNode, res: list):
        if _tree is not None:
            visit(_tree, res)
            pre_order(_tree.left, res)
            pre_order(_tree.right, res)


    def mid_order(_tree: TreeNode, res: list):
        if _tree is not None:
            mid_order(_tree.left, res)
            visit(_tree, res)
            mid_order(_tree.right, res)


    def post_order(_tree: TreeNode, res: list):
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
        left = reconstruct_from_pre_and_mid(pre_order_seq[1: root_pos_in_mid + 1], mid_order_seq[:root_pos_in_mid])
        right = reconstruct_from_pre_and_mid(pre_order_seq[root_pos_in_mid + 1:], mid_order_seq[root_pos_in_mid + 1:])

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
        right = reconstruct_from_post_and_mid(post_order_seq[root_pos_in_mid: -1], mid_order_seq[root_pos_in_mid + 1:])

        root_node.left = left
        root_node.right = right
        return root_node


    print("Reconstruct from post and mid order: ")
    new_tree = reconstruct_from_post_and_mid(post_order_res, mid_order_res)
    print(new_tree == tree)
    new_tree_pre_order_res = []
    pre_order(new_tree, new_tree_pre_order_res)
    [print(_node) for _node in new_tree_pre_order_res]


    def max_depth(root: TreeNode):
        if root is None:
            return 0
        left_height = max_depth(root.left)
        right_height = max_depth(root.right)
        _height = max(left_height, right_height) + 1
        return _height


    print("Max height: ")
    print(max_depth(tree))

    import sys


    def min_depth(root: TreeNode):
        # 空树
        if root is None:
            return 0

        # 确定叶子节点
        if root.left is None and root.right is None:
            return 1

        left_height = sys.maxsize
        right_height = sys.maxsize

        # 如果左右子树不为空，则分别递归计算左右子树的最小深度
        if root.left is not None:
            left_height = min_depth(root.left)
        if root.right is not None:
            right_height = min_depth(root.right)

        # 左右子树的最小深度加一表示考虑root
        _height = min(left_height, right_height) + 1
        return _height


    print("Min height: ")
    print(min_depth(tree))

    print(min_depth(TreeNode(val=1)))


    def sorted_array_to_BST(nums) -> TreeNode:
        if not nums:
            return None
        root_pos = int(len(nums) / 2)

        left_arr = nums[:root_pos]
        right_arr = nums[root_pos + 1:]

        root = TreeNode(nums[root_pos])

        left_tree = sorted_array_to_BST(left_arr)
        right_tree = sorted_array_to_BST(right_arr)

        root.left = left_tree
        root.right = right_tree

        return root


    print('Sorted array to SBT: ')
    test_nums = [-10, -3, 0, 5, 9]
    new_tree = sorted_array_to_BST(test_nums)
    res = []
    mid_order(new_tree, res)
    [print(_) for _ in res]
