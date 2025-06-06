from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root.left and not root.right:
#              return True
#
#         is_valid_bst = True
#         queue = deque([root])
#
#         while queue:
#             node = queue.pop()
#             node_val = node.val
#
#             if node.left:
#                 queue.append(node.left)
#                 left_val = node.left.val
#                 is_valid_bst = True if left_val < node_val else False
#             if node.right:
#                 queue.append(node.right)
#                 right_val = node.right.val
#                 is_valid_bst = True if right_val > node_val else False
#
#             if not is_valid_bst:
#                 return False
#         return is_valid_bst

# Approach 1: Recursive
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)

# Approach 2: Recursive
class Solution:
    def isValidBST(self, root):
        if not root:
            return True

        stack = [(root, -float('inf'), float('inf'))]

        while stack:
            node, low, high = stack.pop()
            if not (low < node.val < high):
                return False
            if node.right:
                stack.append((node.right, node.val, high))
            if node.left:
                stack.append((node.left, low, node.val))

        return True

solution = Solution()

# TestCase 1
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.left = node1
node2.right = node3
print(solution.isValidBST(root=node2))

# TestCase 2
node0 = TreeNode(0)
print(solution.isValidBST(root=node2))

# TestCase 3
node1 = TreeNode(1)
node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node6 = TreeNode(6)

node5.left = node1
node5.right = node4
node4.left = node3
node4.right = node6
print(solution.isValidBST(root=node5))

# TestCase 4
node5 = TreeNode(5)
node4 = TreeNode(4)
node6 = TreeNode(6)
node3 = TreeNode(3)
node7 = TreeNode(7)

node5.left = node4
node5.right = node6
node6.left = node3
node6.right = node7
print(solution.isValidBST(root=node5))

