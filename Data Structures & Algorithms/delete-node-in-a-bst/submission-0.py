# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: leaf node
            if not root.left and not root.right:
                return None
            # Case 2: one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Case 3: two children
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def findMin(self, curr: TreeNode) -> TreeNode:
        while curr.left:
            curr = curr.left
        return curr







