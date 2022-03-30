# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        '''
        
        queue = (0:[3,0],-1:[9,5],-2:[4],1:[8])
        hashmap = 
    
        '''
        if root == None:
            return []
        
        queue = deque([(root,0)])
        hashmap = defaultdict(list)
        min_col = max_col = 0
        
        while queue:
            
            currnode,col = queue.popleft()
            if currnode:
                hashmap[col].append(currnode.val)
                min_col = min(min_col,col)
                max_col = max(max_col, col)
                
                queue.append((currnode.left, col -1))
                queue.append((currnode.right, col+1))
                
        return [hashmap[x] for x in range(min_col,max_col+1)]
            
                
            
            
                
        
       
        
        
            
        
