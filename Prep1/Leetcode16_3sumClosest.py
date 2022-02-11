import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        
        '''
        [-4,-1,1,2] target =1 
          
         abs(target-sum)
         
         seen = set()
         dup = set()
               (-4)

         closest = max.size
         
         diff = target - (nums[i] + nums[j])
         if diff in seen :
            closest = nums[i] + nums[j] + diff
            break
            
         else:
            if  diff < closest:
                closest = diff
          
        
        '''
        
        
        diff = float('-inf')
        i = 0 
        sum1 = 0 
        nums.sort()
        
        while i < len(nums):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                sum1= nums[i] + nums[low] + nums[high]
                if abs(target - sum1) < abs(diff):
                    diff = target - sum1
                if sum1 < target:
                    low+=1
                else:
                    high-=1
            if diff == 0 :
                break
            i+=1
                    
        return target - diff  
            
        
        
        '''
        [-4,-1,1,2] 1 
             i l h
         
         sum1= 2
         diff = -1 
         
          
        '''
        
