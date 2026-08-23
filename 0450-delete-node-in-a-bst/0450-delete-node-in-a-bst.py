# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # No left child
            if not root.left:
                return root.right

            # No right child
            if not root.right:
                return root.left

            # Two children:
            # Find the smallest node in right subtree
            successor = root.right

            while successor.left:
                successor = successor.left

            root.val = successor.val

            # Delete the duplicate successor
            root.right = self.deleteNode(root.right, successor.val)

        return root
        