from typing import List

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


from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = defaultdict(list)
        for ticket in tickets:
            routes[ticket[0]].append(ticket[1])

        for route in routes:
            routes[route] = sorted(routes[route], reverse=False)

        print(routes)
        # result = ["JFK"]
        # while routes[result[-1]]:
        #     for idx, port in enumerate(routes[result[-1]]):
        #         if port in routes or idx == len(routes[result[-1]]) - 1:
        #             hit = routes[result[-1]][idx]
        #             del routes[result[-1]][idx]
        #             result.append(hit)
        #             break

        result = []

        def dfs(f):
            while routes[f]:
                dfs(routes[f].pop(0))
            result.insert(0, f)

        dfs('JFK')

        return result


print(Solution().findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
