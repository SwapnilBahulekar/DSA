from collections import OrderedDict
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        
        '''
        [1,0,1,0,1,0,4,0,4]
                   s 
                     e
         
         
         res = max(res,end - start+1)
         hashmap = {1:0,0:}
         
         res = 6
        '''
        
        start = 0 
        end = 0 
        res = 1
        hashmap = OrderedDict()
        
        if len(fruits) == 0 :
            return 0 
         
        while end < len(fruits):
            if fruits[end] not in hashmap:
                hashmap[fruits[end]] = end
                if len(hashmap) > 2:
                    i,idx = hashmap.popitem(last=False)
                    start = idx + 1  
            else:
                if end == len(fruits)-1:
                    res = max(res,end - start+1)
                del hashmap[fruits[end]]
                hashmap[fruits[end]] = end
            res = max(res,end - start+1)
            end+=1
            
        return res
    
    '''
    Time complexity - O(N)
    Space complexity - O(1)
    '''


    
    
    
            
                    
            
