# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        currnode = root
        stack = []
        res = []
        
        while currnode or stack:
            while currnode:
                stack.append(currnode)
                currnode = currnode.left
                
            currnode = stack.pop()
            res.append(currnode.val)
            currnode = currnode.right
                    
        return res
        
        
        '''
        stack = []
        res = [1,3,2]
        
        '''
        
        
            
        
