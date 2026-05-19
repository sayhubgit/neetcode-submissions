# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : idx for idx, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            rootNode = postorder.pop()
            root = TreeNode(rootNode)

            index = inorder_map[rootNode]

            root.right = helper(index+1, right)
            root.left = helper(left, index-1)

            return root
        
        return helper(0, len(inorder)-1)