# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        res = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr)
            curr = curr.right

        first, second = None, None
        for i in range(len(res)-1):
            if res[i].val > res[i+1].val:
                second = res[i+1]
                if first is None:
                    first = res[i]
                else:
                    break

        first.val , second.val = second.val, first.val 

        
        