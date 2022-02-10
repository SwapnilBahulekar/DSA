class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        '''
        
        [-1, 0 , 1 , 2 , -1 , -4]
             s            e
          
        [-4,-1,-1,0,1,2]
          i  j
        res = []
        '''
        
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:                    # if nums[i] > 0 -> there cannot be 2 numbers greater than 0 in remaining list as list is sorted
                break
            if i == 0 or nums[i-1] != nums[i]: #check duplicate in i
                self.twosum(nums,i,res)
        return res
        
    def twosum(self,nums,i,res):
        hashset = set()
        j = i+1
        while j < len(nums):
            complement = 0 -(nums[i] + nums[j])
            if complement in hashset:
                res.append([nums[i],nums[j],complement])
                while j + 1 < len(nums) and nums[j] == nums[j+1]:   #check repeating elements  
                    j+=1
            hashset.add(nums[j])
            j+=1
            
                
        
        
        
        
            
            
                    
        
        
        
        
        
