class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        '''
        [1,2,3,1,2,2]
        
        
        hashmap - {1:2,2:1,3:2}
        
        map = {1:2,2:3,3:1}
        '''
        
        map = {}     
        for num in nums: 
            if num not in map:
                map[num] = 1
            else:
                map[num]+=1
        print(map)
        
        for val in map:
           
            if map[val] >= 2:
                flag = True
                break 
            else:
                flag= False
                
        return flag 
    
                
        
        
        
        
        
        
