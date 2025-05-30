

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root is None:
#             return []
#         if root.left is None and root.right is None:
#             return [[root.val]]
#
#         node_visit = deque()
#         node_visit.append(root)
#
#         result_list = [[root.val]]
#
#         while node_visit:
#             node_to_visit = node_visit.popleft()
#             if node_to_visit.left:
#                 node_visit.append(node_to_visit.left)
#             if node_to_visit.right:
#                 node_visit.append(node_to_visit.right)
#
#             if node_to_visit.left and node_to_visit.right:
#                 result_list.append([node_to_visit.left.val, node_to_visit.right.val])
#             elif node_to_visit.left:
#                 result_list.append([node_to_visit.left.val])
#             elif node_to_visit.right:
#                 result_list.append([node_to_visit.right.val])
#
#         return result_list

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5


solution = Solution()
assert Solution().levelOrder(node1) == [[1], [2, 3], [4, 5]]