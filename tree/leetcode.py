from tree.basic import TreeNode, tree


def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    if cloned is None:
        return None
    # if cloned.val == target.val:
    if cloned == target:
        # print(id(cloned), id(target))
        return cloned

    left_tree = cloned.left
    right_tree = cloned.right

    res = getTargetCopy(left_tree, left_tree, target)
    if res is not None:
        return res
    res = getTargetCopy(right_tree, right_tree, target)

    return res


# target_node = TreeNode(1)
# target_node = TreeNode(2)
target_node = TreeNode(3)
f = TreeNode(6)
target_node.left = f
# target_node = TreeNode(4)
# target_node = TreeNode(5)
# target_node = TreeNode(6)

print(getTargetCopy(tree, tree, target_node))
# print(getTargetCopy(tree, tree, tree))
